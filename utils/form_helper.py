def create_attributes(placeholder='', classes=[]):
    attrs = {'placeholder': placeholder, 'class': 'un'}
    attrs['class'] += ' '.join(classes)
    attrs['align'] = 'center'
    return attrs
