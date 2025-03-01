# Models
1. BaseModel
    - create_date : DateTime auto_now_add
    - write_date : DateTime auto_now_add
    - archived : Boolean : Default False

2. Item
    - name : CharField
    - description : TextField
    - price : FloatField
    - stock_qty : PositiveInteger
    - height : PositiveInteger : nullable
    - width : PositiveInteger : nullable
    - weight : PositiveInteger : nullable
    - barcode : CharField (11 digit symbol, auto generated) : unique
    - expiration_date : DateField
    - category m2o -> Category

3. Category
    - name : CharField


## Endpoints

- 'items/' GET
- 'items/' POST
- 'items/<int:id>' GET
- 'items/<int:id>' PUT
- 'items/<int:id>' PATCH
- 'items/<int:id>' DELETE
- 'categories/' GET
- 'categories/' POST
- 'categories/<int:id>' GET 
- 'categories/<int:id>' PUT 
- 'categories/<int:id>' PATCH 
- 'categories/<int:id>' DELETE
