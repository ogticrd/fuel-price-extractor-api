# Fuel price extractor

This is an service that extract the price of the fuel in RD from [micm history fuel prices pdf](https://micm.gob.do/direcciones/combustibles/avisos-semanales-de-precios/aviso-semanal-de-precios-de-combustibles-version-12-11-2021).

## Install

```console
$ docker build -t fuel-extractor .
$ docker run -d -p 8080:80 fuel-extractor
```

## How to use it

```console
$ curl http://localhost:8080/prices
{
    "Gasolina Premium": "287.60",
    "Gasolina Regular": "270.50",
    "Gasoil Regular": "217.60",
    "Gasoil Regular EGP-C ( Inter. y No Interconectado)": "201.20",
    "Gasoil Regular EGP-T ( Inter. y No Interconectado)": "195.52",
    "Gasoil Optimo": "236.10",
    "Avtur": "198.98",
    "Kerosene": "227.60",
    "Fuel Oil": "162.95",
    "Fuel Oil EGP-C ( Inter. y No Interconectado)": "160.58",
    "Fuel Oil EGP-T ( Inter. y No Interconectado)": "154.90",
    "Fuel Oil 1% Azufre (FO6, 1%S)": "180.29",
    "Fuel Oil 1% Azufre (FO6, 1%S) EGP-C ( Inter. y No Interconectado)": "177.92",
    "Fuel Oil 1% Azufre (FO6, 1%S) EGP-T ( Inter. y No Interconectado)": "172.24",
    "Gas Licuado de Petróleo (GLP) **": "147.60",
    "Cilindros de 100 Libras (25.00 Gls. Max.)***": "3,690.06",
    "Cilindros de 50 Libras (12.50 Gls. Max.)": "1,845.03",
    "Cilindros de 25 Libras  (6.25 Gls. Max.)": "922.52",
    "Cilindros de 15 Libras (3.75 Gls. Max.)": "553.51"
}
```
