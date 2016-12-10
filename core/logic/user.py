from base import BaseObject
from core.models import session
from core.models import User as UserModel


class User(BaseObject):
    def __init__(self, pk, model=None):
        super(User, self).__init__(pk)
        self._model = model
	self._info = None

    def _lazy_load_user(self):
	if self._info == None:
	    if self._model == None:
	        self._model = UserModel.filter_by(session=session, id=self._pk).first()

		self._info = {
		    'name': self._model.name,
		    'avatar': self._model.avatar_url,
		    'latitude': self._model.latitude,
		    'longitude': self._model.longitude
		}
		if self._info['latitude'] == None:
		    self._info['latitude'] = 0
		if self._info['longitude'] == None:
		    self._info['longitude'] = 0

    def info(self):
        self._lazy_load_user()
        super_info = super(User, self).info()
        model = self._model
        super_info.update({
            'name': model.name,
            'avatar': model.avatar_url
        })
        return super_info

    @property
    def name(self):
        self._lazy_load_user()
        return self._info['name']

    @property
    def latitude(self):
        self._lazy_load_user()
        return self._info['latitude']

    @property
    def longitude(self):
        self._lazy_load_user()
        return self._info['longitude']

    @classmethod
    def sign_up(cls, **kwargs):
        user_model = UserModel()
        user_model.email = kwargs['email']
        user_model.telphone = kwargs['telphone']
        user_model.password = kwargs['password']
        user_model.user_name = kwargs['user_name']

        session.add(user_model)
        session.commit()

    @classmethod
    def sign_in(cls, email=None, telphone=None, password=None):
        user_model_list = session.query(UserModel).filter_by(email=email, telphone=telphone).all()
        if len(user_model_list) > 0:
            user_model = user_model_list[0]
            if cls.__check_password(password, user_model.password):
                return cls(user_model.id, user_model)
            else:
                return None
        else:
            return None

    @classmethod
    def __check_password(cls, check, from_db):
        return check == from_db

    @classmethod
    def filter(cls, **kwargs):
        user_model_list = UserModel.filter_by(session=session, **kwargs).all()
        user_object_list = []
        for item in user_model_list:
            user_object_list.append(cls(item.id, model=item))
        return user_object_list
