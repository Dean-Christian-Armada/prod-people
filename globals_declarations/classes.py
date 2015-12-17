from django.utils.safestring import mark_safe
from django.forms.formsets import BaseFormSet
from django import forms

# Renders manually made for horizontal selections
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class HorizontalCheckboxRenderer(forms.CheckboxSelectMultiple.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

# Enables field required on formset even without filling up a singlefield
class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

# Enables field required on the first form
class FirstRequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(FirstRequiredFormSet, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False