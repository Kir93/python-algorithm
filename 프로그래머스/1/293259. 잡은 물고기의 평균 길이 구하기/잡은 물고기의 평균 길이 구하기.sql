-- 코드를 작성해주세요
select round(avg(if(LENGTH <= 10 or LENGTH is null, 10, LENGTH)), 2) as AVERAGE_LENGTH from FISH_INFO