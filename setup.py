from distutils.core import setup
from svc_utils import SvcUtils

setup(
    name='message_service',
    packages=['message_service'],
    version=SvcUtils.get_build_version(),
    description='Message Service',
    url='https://github.com/EnzoGunn/message_service',
    author='Ahmad Saeed'
)
