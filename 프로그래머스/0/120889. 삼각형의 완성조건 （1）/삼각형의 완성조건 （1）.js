function solution(sides) {
    const maxV = Math.max(...sides)
    
    if(sides.reduce((acc, cur) => acc + cur) - maxV > maxV) return 1
    else return 2
}