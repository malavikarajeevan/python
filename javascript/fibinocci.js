function fibonocci(n)
{
    let fibonocciseries=(0,1);
    for(let i=2;i<n;i++)
    {
        fibonocciseries(i)=fibonocciseries(i-1)+fibonocciseries(i-2)
    }
    return fibonocciseries;

}
result=fibonocci(10);
console.log(result)
