from urllib import urlencode
from urlparse import urlparse
import drest
from drest.exc import dRestRequestError, dRestError
from requests.utils import parse_header_links
from django.http import QueryDict
from getenv import env
from dce_course_info import settings

import logging
log = logging.getLogger(__name__)

API_PATH = '/api/course/v2/'

class CourseUpdateError(dRestRequestError):
    pass

class ICommonsApi(drest.API):

    @classmethod
    def from_request(cls, request):
        icommons_base_url = settings.ICOMMONS_BASE_URL
        access_token = settings.ICOMMONS_API_TOKEN
        return cls(icommons_base_url, access_token)


    def __init__(self, icommons_base_url, access_token):
        self.icommons_base_url = icommons_base_url
        self.headers = {'Authorization': "Token %s" % access_token,
                        'Content-Type': 'application/json'}
        super(ICommonsApi, self).__init__(icommons_base_url + API_PATH,
                                        extra_headers=self.headers,
                                        timeout=60,
                                        serialize=True,
                                        trailing_slash=False)


    def get_course_info(self, course_instance_id):
        course_info={}
        try:
            relative_url = '/course_instances/'+ course_instance_id+'/?format=json'
            response = self.make_request('GET',relative_url,headers=self.headers)
            course_info = response.data.copy()
        except drest.exc.dRestRequestError as e:
            log.error(e.message)
        except Exception as e:
            log.error(e.message)
        return course_info



