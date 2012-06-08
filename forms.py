from wtforms import Form, SelectField
import choices

class CertificateForm(Form):
    email = SelectField(u'Do you email your users their passwords?', choices=choices.EMAILING, default=1, coerce=int)
    hashing = SelectField(u'Do you use a hash?', choices=choices.HASHING, default=3, coerce=int)
    salting = SelectField(u'Do you salt those passwords?', choices=choices.SALTING, default=2, coerce=int)
    
