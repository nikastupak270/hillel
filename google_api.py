import jinja2
import requests
import smtplib
import ssl


def render_html(html_path: str, params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(html_path)
    output = template.render(params)
    return output


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

result = render_html('templates/animal_info.html', most_costed_animal)
msg = f'''From: nika.stupak.2013@gmail.com
         Subject: Найбільш дорога в обслуговуванні тварина
         {result}
         '''
password = input('Input your password: ')
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login('nika.stupak.2013@gmail.com', password)
    server.sendmail(
        'nika.stupak.2013@gmail.com', 'nika.stupak.2013@gmail.com', msg
    )
