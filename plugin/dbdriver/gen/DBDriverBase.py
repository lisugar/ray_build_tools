import six
import abc
import os

@six.add_metaclass(abc.ABCMeta)
class BaseDBDriver(object):

    @abc.abstractmethod
    def create_resource(self, ctx, obj_type, request_dict):
        raise NotImplementedError('BaseDBDriver should implement the method to execute')  # pragma: no cover

    @abc.abstractmethod
    def read_resource(self, ctx, obj_type, id):
        raise NotImplementedError('BaseDBDriver should implement the method to execute')  # pragma: no cover

    @abc.abstractmethod
    def update_resource(self, ctx, obj_type, request_dict):
        raise NotImplementedError('BaseDBDriver should implement the method to execute')  # pragma: no cover

    @abc.abstractmethod
    def list_resource(self, ctx, obj_type, filter={}):
        raise NotImplementedError('BaseDBDriver should implement the method to execute')  # pragma: no cover

    @abc.abstractmethod
    def delete_resource(self, ctx, obj_type, id):
        raise NotImplementedError('BaseDBDriver should implement the method to execute')  # pragma: no cover