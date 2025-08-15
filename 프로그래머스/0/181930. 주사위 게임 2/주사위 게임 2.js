function sum(a, b, c){
    return [a,b,c].reduce((acc, cur) => acc += cur)
}

function solution(a, b, c) {
    let flag = [...new Set([a, b, c])].length
    
    if(flag === 3){
        return sum(a, b, c)
    }else if(flag === 2){
        return sum(a, b, c) * sum(a**2, b**2, c**2)
    }else{
        return sum(a, b, c) * sum(a**2, b**2, c**2) * sum(a**3, b**3, c**3)
    }
}