---
layout: post
disqus: y
title: HTML Styles
---

### HTML Styles

Atributul HTML "style"  este folosit pentru a adauga stiluri unui element HTML. De exemplu: color, size, alignment, etc.

```html
<!DOCTYPE html>
<html>
<body>

<p>I am normal</p>
<p style="color:red;">Sunt rosu</p>
<p style="color:blue;">Sunt albastru</p>
<p style="font-size:50px;">Sunt mare</p>

</body>
</html>

```

HTML Style Attribute
-----------

Setarea stilului unui element HTML se poate realiza cu "style" attribute.

The HTML style attribute are urmatoarea sintaxa:

```html
   <tagname style="property:value;">
```

- property is a CSS proprietate.
- value este un CSS valoare.

#### Background Color

Setam CSS background-color background-ul unei pagini cu blue:

```html
<!DOCTYPE html>
<html>
<body style="background-color: blue;">

<h1>Acesta este un heading</h1>
<p>Acesta este un paragraph.</p>

</body>
</html>
```

Proprietatea CSS background-color seteaza culoarea de fond pentru un element.

```html
<!DOCTYPE html>
<html>
<body>

<h1 style="background-color: orange">Acesta este un heading</h1>
<p style="background-color: lightblue">Acesta este un paragraph.</p>

</body>
</html>
```
#### Text Color

Proprietatea CSS color defineste text color-ul pentru un element HTML

```html
<!DOCTYPE html>
<html>
<body>

<h1 style="color:blue;">Acesta este un heading</h1>
<p style="color:red;">Acesta este un paragraph.</p>

</body>
</html>

```

#### Fonts

Proprietatea CSS font-family defineste tipul fontului folosit pentru un anumit HTML element.

```html
<!DOCTYPE html>
<html>
<body>

<h1 style="font-family:verdana;">This is a heading</h1>
<p style="font-family:courier;">This is a paragraph.</p>

</body>
</html>
```


#### Text Size

Proprietatea CSS font-size defineste size-ul unui element.

```html
<!DOCTYPE html>
<html>
<body>

<h1 style="font-size:300%;">Acesta este un heading</h1>
<p style="font-size:160%;">Acesta este un paragraph.</p>

</body>
</html>
```

#### Text Alignment

Proprieatea CSS text-align defineste "orizontal" alinierea textului pentru un HTML Element.

exemplu: text-align: center, left, right.

```html
<!DOCTYPE html>
<html>
<body>

<h1 style="text-align:center;">Centered Heading</h1>
<p style="text-align:center;">Centered paragraph.</p>

</body>
</html>
```

Rezumatul capitolului:

- foloseste atributul "style" pentru stilizarea unui HTML Element.
- foloseste proprietatea CSS background-color pentru background
- foloseste proprietatea CSS color pentru culoarea textului.
- foloseste proprietatea CSS font-family pentru tipul fontului(verdana, arial, courier, etc).
- foloseste proprietatea CSS font-size pentru marimea textului.
- foloseste proprietatea CSS text-align pentru alinierea textului.

