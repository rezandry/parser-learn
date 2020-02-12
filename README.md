Question :
```
Gunakan parser.py untuk membuat parser format inputan yang berbeda antara satu agent dengan agent lainnya
```

Story :
```
Kita adalah perusahaan agregator, terdapat 3 agent yang akan bekerja sama dengan kita, sebagai agregator, kita akan menerima inputan dari agent, lalu akan kita jadikan satu format yang sama untuk bisa diproses. 
Akan ada 3 format data untuk berkomunikasi dengan kita, yakni SMS, XML dan JSON.
```

Format Input :
- Jalur SMS : 
> TOPUP XL100 085642405493

- Jalur XML :
```xml
<payload>
    <action>TOPUP</action>
    <denom>XL100</denom>
    <phonenumber>085642405493</phonenumber>
</payload>
```

- Jalur JSON :
```json
{
    "action":"TOPUP",
    "denom":"XL100",
    "phonenumber":"085642405493"
}
```

Format Output :
```json
{
    "transaction_type":"TOPUP",
    "denom":"XL100",
    "phone_number":"085642405493"
}
```

referensi : 
- https://docs.python.org/2/library/xml.etree.elementtree.html
- https://www.w3schools.com/python/ref_string_split.asp
- https://medium.com/better-programming/25-useful-python-snippets-to-help-in-your-day-to-day-work-d59c636ec1b
- https://code.sololearn.com/cOAXyhEmN1f7