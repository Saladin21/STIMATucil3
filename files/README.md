# Tucil Stima 3 Mantap
> beban Tubes deadline Tucil

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
projek untuk membuat algoritma Path Finder A* menggunakan google maps API

## Setup
disclaimer: jalankan perintah ini pada folder utama(STIMATucil3)  
buat virtual environtment, install flask, dan jalankan:  
`$ pip install virtualenv`  
`$ virtualenv env`  
`$ .\env\Scripts\activate`  
`$ (env) pip install flask`

## Features
terdapat 2 macam input yaitu:
* input dari file, terdapat 2 file yaitu file graph dan file matriks
* input langsung dari google maps  

pada halaman hasil terdapat juga pilihan untuk menyimpan input dalam bentuk:
* file graph
* file matriks

## How to Use
file input terdiri dari 2 file yaitu file matriks dan file graph yang memiliki format txt. nama dari file graph harus didului oleh "Graph" sedangkan nama dari file matriks didului oleh "Matriks". isi dari file graph adalah baris pertama yang menyatakan jumlah simpul n, dan n baris selanjutnya yang menyatakan simpul dengan format langitude<spasi>latitude<spasi>nama simpul.  
contoh:

`10  
-6.892659329143158 107.61042200983438 Pintu Utama ITB  
-6.892622915818573 107.60874173131332 Simpang Aula Barat  
-6.89245443845861 107.61187380880716 Simpang Aula Timur`<br />
## Inspiration
Add here credits. Project inspired by..., based on...

## Contact
Created by Syihabuddin Yahya Muhammad - 13519149 dan Ahmad Saladin - 13519187
