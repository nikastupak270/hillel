import requests
import smtplib
import ssl

url = 'https://script.google.com/macros/s/AKfycbxp6aZAg7HXs7y8Uei1T6FiVHZdEpoFTa5Rs20w8aoSObSsLXuqplOFhbf5mGArDnIU/exec'

response = requests.get(url).json()

cost_of_care_poisoned = 0
qty_african = 0
most_costed_animal = None
for animal_item in response['data']:
    if animal_item['is_poisoned']:
        cost_of_care_poisoned += animal_item['price'] * animal_item['qty']
    if animal_item['from'] == 'Африка':
        qty_african += animal_item['qty']
    if not most_costed_animal or most_costed_animal['price'] < animal_item['price']:
        most_costed_animal = animal_item
print(f'Вартість догляду за отруйними тваринами: {cost_of_care_poisoned}')
print(f'Кількість африканських тварин в зоопарку: {qty_african}')

title = f'<h3>{most_costed_animal['title']}</h3>' if most_costed_animal['is_poisoned'] else f'<h4>{most_costed_animal['title']}</h4>'
msg = f'''From: nika.stupak.2013@gmail.com
         Subject: Найбільш дорога в обслуговуванні тварина
         Title - {title}
         Cost of care - {most_costed_animal['price']}
         Quantity - {most_costed_animal['qty']}
         From - {most_costed_animal['from']}
         '''
password = input('Input your password: ')
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login('nika.stupak.2013@gmail.com', password)
    server.sendmail(
        'nika.stupak.2013@gmail.com', 'nika.stupak.2013@gmail.com', msg
    )
