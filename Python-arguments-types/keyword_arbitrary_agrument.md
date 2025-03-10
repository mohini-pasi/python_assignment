```python
def keyword_arbitrary_agrument(**kargs):
    sum = 0
    for key,values in kargs.items():
        if isinstance (values,int):
            sum = sum + values
    return sum
data=keyword_arbitrary_agrument(a=100,b=200,c=300,d=400,e=500)
print(data)
```
#output 1500
