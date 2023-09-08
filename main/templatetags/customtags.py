from django import template

register = template.Library()

@register.filter(name='split')
def split(value):
  # Separate on comma.
  splitter = value.split(",")

  # # Loop and print each string.
  # for s in splitter:
  #     return(s)
  return splitter
