import requests
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)

url = "https://love-calculator.p.rapidapi.com/getPercentage"

print("ponga un nombre:")
nombre1 = input()
print("ponga otro nombre:")
nombre2 = input()

querystring = {"sname":nombre1,"fname":nombre2}

headers = {
	"X-RapidAPI-Key": "f45575bd09msh5d28c6e6ce6f035p1aaee8jsn09a2b35a5da8",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

edit = response.json()
text = edit["sname"]+" y "+edit["fname"]+" son un "+edit["percentage"]+" compatibles, "+edit["result"]

pdf.cell(200, 10, txt = text,
         ln = 1, align = 'C')

pdf.output("match.pdf")

print(response.json())

#MIRAR EL ENVIROMENT EN VSCODE Y ABRIRLO CON LA EXTENSION DE PDF DE VSCODE O POR APARTE EN LA CARPETA DONDE SE CREO
