__author__ = 'Max Buck'
__email__ = 'maxbuckdeveloper@gmail.com'
__version__ = '1.0.0'

from neomodel import (StringProperty, AliasProperty, RelationshipTo, Relationship, ZeroOrOne)
#from serializable_structured_node import SerializableStructuredNode
from neoapi import SerializableStructuredNode

class User(SerializableStructuredNode):
    """
    This is an example class for showing how a SerializableStructuredNode is put together. ALL rules for StructuredNode\
    apply to SerializableStructuredNode.  Please refer to the NeoModel documentation at \
    http://neomodel.readthedocs.org/en/latest/.
    """

    __index__ = 'User'

    # INFO
    version = '1.0.0'  # => A version is not required but is a good idea
    secret = ['password']  # => Variable names listed in this list don't show up in resource objects returned by the API
    hashed = ['password']  # => Variable names listed in this list are encrypted using sha256
    enums = {'gender': ['m', 'f', 'o']}  # => Enums in this dictionary can only be
    dates = ['birthday']  # => Format datetime object as date because datetime.date objects cannot be json encoded

    # ATTRIBUTES -- NOTE: 'type' and 'id' are required for json api specification compliance
    type = 'users'  # => The type attribute is required for all SerializableStructuredNodes
    id = AliasProperty(to='email')  # => The id attribute is also required
    email = StringProperty(unique_index=True, required=True)
    password = StringProperty(required=True)
    gender = StringProperty()
    
    # RELATIONSHIPS
    friends = Relationship('User', 'HAS_FRIEND')
    mom = RelationshipTo('User', 'HAS_MOM', cardinality=ZeroOrOne)
