Plik README.md w projekcie jest ważnym elementem dokumentacji, który pomaga użytkownikom zrozumieć, jak korzystać z projektu.

Pliki Markdown (o rozszerzeniu .md) są formatowane przy użyciu składni Markdown. Markdown to lekki język znaczników, który został stworzony z myślą o prostocie i czytelności w zwykłym tekście, ale jednocześnie umożliwia konwersję do HTML.

Aby uzyskać więcej informacji na temat składni ->
[Markdownguide](https://www.markdownguide.org/)

Poniżej przykładowy plik .MD który może być wygenerowany dla projektu.

# Symulator Zbiornika Wody z Grzałką

Projekt Pythona mający na celu symulację działania zbiornika wody z grzałką. Zbiornik umożliwia operacje takie jak nalewanie i wylewanie wody, podgrzewanie wody oraz mieszanie ciepłej i zimnej wody. Udostępnia interfejs przy użyciu REST API poprzez moduł Flask w Pythonie.

## Spis Treści
- [Instalacja](#instalacja)
- [Uruchomienie](#uruchomienie)
- [Dokumentacja API](#dokumentacja-api)
- [Przykłady](#przykłady)
- [Informacje o Licencjach](#info)
- [Autor](#autor)


## Instalacja

Aby zainstalować projekt, wykonaj poniższe kroki:

1. Sklonuj repozytorium:
    ```bash
    git clone "zastąp linkiem do repozytorium"
    ```
2. Stwórz virtualne środowisko:
    ```bash
    python -m venv .venv
    ```

3. Zainstaluj potrzebne pakiety:
    ```bash
    pip install -r requirements.txt
    ```
## Uruchomienie
Uruchom projekt za pomocą poniższego polecenia:
```bash
python main.py
```
*Aplikacja domyślnie zostanie uruchomiona pod adresem: http://localhost:5000/*

> Uwaga aplikacja udostępnia port w sieci, aby to zmienić usuń **host='0.0.0.0'**, wtedy aplikacją będzię uruchomiona tylko lokalnie

## Dokumentacja API

W projekcie jest udostępniony swagger, ktory jest dostępny po uruchomnieniu proektu, pod adresem http://localhost:5000/apidocs/

## Przykłady użycia

Uruchomienie grzałki:
```bash
curl -X POST localhost:5000/heater -H "Content-Type: application/json" -d "{\"state\": true}"
```


## Informacje o Licencjach
Projekt kożysta z poniższych modułów:

| Moduł | Link do strony projektu | Licencja|
| ----------- | ----------- | ----------- |
| Flask | https://flask.palletsprojects.com/en/3.0.x/ |[BSD-3-Clause](https://flask.palletsprojects.com/en/3.0.x/license/)|
| Flasgger | https://github.com/flasgger/flasgger/blob/master/README.md | [MIT](https://github.com/flasgger/flasgger/blob/master/LICENSE)

## Autor

Autor Projektu