from wtforms import Form, SelectField
import choices
from choices import remove_score

class CertificateForm(Form):
    email = SelectField(u'Do you email your users their passwords?', choices=remove_score(choices.EMAILING))
    hashing = SelectField(u'Do you use a hash?', choices=remove_score(choices.HASHES))
    salting = SelectField(u'Do you salt those passwords?', choices=remove_score(choices.SALTING))
    
