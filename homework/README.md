# Как запустить
0) (*) Удалить существующие файлы `pulls*`
1) Выполнить python скрипт `python3 homework/getpulls.py [url]`. 
   Он скачает по заданному url страницу с pull requests в файл `homework/pulls.html`.
   По умолчанию url страницы `https://github.com/facebook/create-react-app/pulls?q=is%3Apr`
   Дополнительно скрипт создаст модификацию скаченного файла `homework/pulls-valid.html` - это исходный файл
   в котором выкинута неинтересная часть с невалидным html.
2) Запустить `xsltproc --output homework/pulls.xml homework/make-xml.xsl homework/pulls-valid.html`
   для генерации `xml` файла по скачанной старнице.
3) Запустить `xsltproc --output homework/pulls-result.html homework/make-html.xsl homework/pulls.xml`
   для генерации `html` страницы по сгенерированному `xml`.

```bash
for f in homework/pull#*; do xsltproc --output  "${f%*.html}.xml" homework/make-html-single.xsl $f; done
```
