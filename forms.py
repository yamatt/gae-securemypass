from wtforms import Form, SelectField
import choices

class CertificateForm(Form):
    email = SelectField(u'Do you email your users their passwords?', choices=choices.EMAILING, coerce=int)
    hashing = SelectField(u'Do you use a hash?', choices=choices.HASHES, coerce=int)
    salting = SelectField(u'Do you salt those passwords?', choices=choices.SALTING, coerce=int)
    
