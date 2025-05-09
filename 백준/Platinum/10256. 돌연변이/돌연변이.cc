#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef tuple<int, int, int> tiii;

const int MAXTR = 1000001;
const int MAXAL = 4;
int N, M;
string DNA, marker;

int node = 1;
int root = 0;
int trie[MAXTR][MAXAL];
bool exist[MAXTR];
int fail[MAXTR];

queue<int> qu;

void init()
{
    node = 1;
    memset(trie, -1, sizeof(trie));
    memset(exist, false, sizeof(exist));
    memset(fail, -1, sizeof(fail));
}

int getVal(char c)
{
    if(c == 'A') return 0;
    if(c == 'C') return 1;
    if(c == 'G') return 2;
    return 3;
}

void solve()
{
    init();
    
    cin >> N >> M;
    cin >> DNA >> marker;
       
    for(int i=0; i<M; i++)
    {
        for(int j=i; j<M; j++)
        {
            int curNode = root;
            char c;
            for(int k=0; k<M; k++)
            {
                if(k < i || k > j) c = marker[k];
                else c = marker[j-k+i];
                
                if(trie[curNode][getVal(c)] == -1) trie[curNode][getVal(c)] = node++;
                curNode = trie[curNode][getVal(c)];
            }
            exist[curNode] = true;
        }
    }
    
    fail[root] = root;
    qu.push(root);
    while(!qu.empty())
    {
        int curNode = qu.front(); qu.pop();
        for(int i=0; i<MAXAL; i++)
        {
            int& childNode = trie[curNode][i];
            if(childNode == -1) continue;
            
            int failNode = fail[curNode];
            if(curNode != root)
            {
                while(failNode != root && trie[failNode][i] == -1) failNode = fail[failNode];
                if(trie[failNode][i] != -1) failNode = trie[failNode][i];
            }
            
            fail[childNode] = failNode;
            if(exist[failNode]) exist[childNode] = true;
            qu.push(childNode);
        }
    }
    
    int ans = 0;
    int curNode = root;
    for(char c : DNA)
    {
        while(curNode != root && trie[curNode][getVal(c)] == -1) curNode = fail[curNode];
        if(trie[curNode][getVal(c)] != -1) curNode = trie[curNode][getVal(c)];
        if(exist[curNode]) ans++;
    }
    
    cout << ans << "\n";
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    
    int T; cin >> T;
    while(T--) solve();
}