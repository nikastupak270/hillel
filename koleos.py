koleos_base = {
    'title': 'Бензин 2,5 (171 к.с.) 4х2 АКП (CVT)',
    'price': 1_263_400,
    'has_rear_dynamic_led_lights': False,
    'has_sunroof': {},
    'has_rails_on_the_roof': True,
    'has_cover_on_the_bumper': True,
    'has_additional_tinting_of_rear_windows': True,
    'has_18_inch_discs': True,
    'has_metallic_paint': {'price': 19596},
    'has_special_black_amethyst_paint': {},
    'exterior_features': [
        'rails on the roof',
        'cover on the bumper',
        'additional tinting of rear windows',
        '18 inch discs',
        'metallic paint'
    ]
}
koleos_intense = {
    'title': 'Бензин 2,5 (171 к.с.) 4х4 АКП (CVT)',
    'price': 1_470_800,
    'has_rear_dynamic_led_lights': True,
    'has_sunroof': {'price': 29486},
    'has_rails_on_the_roof': True,
    'has_cover_on_the_bumper': True,
    'has_additional_tinting_of_rear_windows': True,
    'has_18_inch_discs': True,
    'has_metallic_paint': {'price': 19596},
    'has_special_black_amethyst_paint': {'price': 21758},
    'exterior_features': [
        'rails on the roof',
        'cover on the bumper',
        'additional tinting of rear windows',
        '18 inch discs',
        'metallic paint',
        'special black amethyst paint'
    ]
}


def print_sunroof_price(item):
    print('Sunroof price is: ', item['has_sunroof'].get('price', None))


def print_exterior_features(item):
    print('Exterior features:')
    for feature in item['exterior_features']:
        print(f'- {feature}')


print_sunroof_price(koleos_intense)
print_exterior_features(koleos_base)
print_exterior_features(koleos_intense)
