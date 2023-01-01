# Testando o pacote phonenumber_field

Testando o pacote `phonenumber_field`. Este pacote disponibiliza o `model`, `form`, `serializer` e `validação` para números de telefones internacionais. O pacote utiliza `phonenumbers` outro pacote python. O phonenumbers por sua vez é um port de uma biblioteca do `Google`.

# Forms

O `form` foi testado em uma view no `/`. Onde podemos criar um telefone via `post`. A view também lista os telefonos no banco de dados.

# API

## Criando Telefone

> Telefone válido

Request:

```console
curl -i -d '{"number":"+552122814364"}' -H "Content-Type: application/json" POST http://localhost:8000/api/phones/
```

Response:

```javascript
{
    "number":"+552122814364"
}
```

> Telefone inválido

Request:

```console
curl -d '{"number":"value1"}' -H "Content-Type: application/json" POST http://localhost:8000/api/phones/
```

Response:

```javascript
{
    "number":["The phone number entered is not valid."]
}
```


## Listando Telefones

> Listando os telefone

Request:

```console
curl -i -X GET http://localhost:8000/api/phones/
```

Response:

```javascript
[
    {
        "id":12,
        "number":"+552122814365"
    },
    {
        "id":16,
        "number":"+552122814365"
    },
```

## Deletando Telefone

```console
curl -i -X DELETE http://localhost:8000/api/phones/12/
```
