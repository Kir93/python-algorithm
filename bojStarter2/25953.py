import io, os, sys

inf = sys.maxsize


def main() -> None:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    num_nodes, timesteps, num_edges = map(int, input().split())
    start, end = map(int, input().split())
    dists = [inf] * num_nodes
    dists[start] = 0
    for _ in range(timesteps):
        new_dists = dists[:]
        for _ in range(num_edges):
            u, v, w = map(int, input().split())
            if dists[u] + w < new_dists[v]:
                new_dists[v] = dists[u] + w
            if dists[v] + w < new_dists[u]:
                new_dists[u] = dists[v] + w
        dists = new_dists
    if dists[end] < inf:
        print(dists[end])
    else:
        print(-1)


if __name__ == "__main__":
    sys.exit(main())