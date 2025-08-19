function solution(my_string, index_list) {
    return index_list.map(i => my_string[i]).join('');
}