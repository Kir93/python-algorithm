function solution(num_list) {
    let odd = even = ''
    
    for (num of num_list){
        if(num%2 === 0){
            even += String(num)
        } else {
            odd += String(num)
        }
    }
    
    return parseInt(odd, 10) + parseInt(even, 10)
}