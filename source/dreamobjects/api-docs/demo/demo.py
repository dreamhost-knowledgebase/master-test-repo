#!/usr/bin/env python
'''
DreamObjects Demo
'''
from uuid import uuid4 as uuid
from inspect import cleandoc

import webbrowser
import sys
import argparse

# import required third-party modules
try:
    # termcolor is NOT packaged in Ubuntu 12.04
    # Users on shared servers cannot install Python packages themselves, so
    # simply fall back to uncolored output.
    from termcolor import colored # pylint: disable=wrong-import-position
except ImportError:
    def colored(string, color, **kwargs): # pylint: disable=unused-argument
        '''Fallback version of termcolor.colored()'''
        return string

missing_packages = [] # pylint: disable=invalid-name
try:
    import boto # pylint: disable=wrong-import-position
    import boto.s3.connection # pylint: disable=wrong-import-position
except ImportError:
    missing_packages += ['boto']


if len(missing_packages) > 0:
    print 'This demonstration requires some packages that are missing.'
    print 'You can use your distribution package manager and local name'
    print 'for the package, or try the pip installer.'
    print ''
    print 'To continue, please install these packages:'
    print '   $ pip install '+(' '.join(missing_packages))
    sys.exit(1)

class OrderedStep(object): # pylint: disable=too-few-public-methods
    '''
    A decorator to step up a list of ordered steps in our demo,
    and store some metadata about those steps.
    '''

    steps = []

    def __init__(self, title=None, prompt=True):
        self.title = title
        self.prompt = prompt

    def __call__(self, method):
        method.title = self.title
        method.prompt = self.prompt
        self.steps.append(method)
        return method


class DreamObjectsDemo(object): # pylint: disable=too-many-instance-attributes
    '''
    DreamObjects Demo
    '''

    # pylint: disable=too-many-arguments
    def __init__(self,
                 access_key,
                 secret_key,
                 bucket_name,
                 object_name,
                 use_s3=False,
                 show_http_traffic=False):
        '''
        Set up all instance variables.
        '''
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.use_s3 = use_s3
        self.show_http_traffic = show_http_traffic
        # These variables are use for state:
        self.public_url = None
        self.signed_url = None
        self.bucket = None
        self.key = None
        self.conn = None

    @OrderedStep()
    def intro(self):
        '''
        DreamObjects Interactive Demo
        =============================

        This demonstration will walk through the process of creating a bucket,
        storing objects in the bucket, setting permissions on objects, deleting
        objects and buckets, and even viewing objects by URL in your web
        browser.
        '''

    @OrderedStep('Creating connection to DreamObjects')
    def create_connection(self):
        '''
        Connecting to DreamObjects
        --------------------------

        DreamObjects can be connected to via the Amazon S3 protocol. By
        supplying an "access key" and a "secret key", and setting the hostname
        for connections to "objects-us-west-1.dream.io", you can use most standard
        Amazon S3 access libraries.

        This demonstration is implemented in Python, with the Boto library.

        Credentials used for this demo:
            Access Key: {access_key}
            Secret Key: {secret_key}
        '''

        kwargs = dict(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            )

        if self.show_http_traffic:
            kwargs['debug'] = 2

        if not self.use_s3:
            kwargs['host'] = 'objects-us-west-1.dream.io'

        # create a connection via the S3 protocol to DreamObjects
        self.conn = boto.connect_s3(**kwargs)

    @OrderedStep('Creating bucket')
    def create_bucket(self):
        '''
        Creating Buckets
        ----------------

        DreamObjects supports the standard notions of "buckets" and "objects".
        Bucket names are globally unique, so for the purposes of this demo,
        we'll be generating a sample bucket name that should be available:

            Bucket Name: {bucket_name}
        '''

        self.bucket = self.conn.create_bucket(self.bucket_name)

    @OrderedStep('Storing object in bucket')
    def store_object(self):
        '''
        Creating Objects
        ----------------

        Objects live inside buckets and represent a chunk of data, which
        frequently correspond to files. In this case, we're going to store
        an object inside the bucket that is the DreamHost logo in PNG
        format. Object names are unique within a bucket.

            Object Name: {object_name}
        '''

        self.key = self.bucket.new_key(self.object_name)
        self.key.set_contents_from_filename(self.object_name)

    @OrderedStep('Getting public reference to object')
    def get_public_reference(self):
        '''
        Linking to Objects
        ------------------

        Objects can be referenced by a public URL, which is of the format:

            http://<bucket-name>.objects-us-west-1.dream.io/<object-name>

        The URL for our object will thus be:

            http://{bucket_name}.objects-us-west-1.dream.io/{object_name}
        '''

        self.public_url = self.key.generate_url(
            expires_in=0,
            query_auth=False,
            force_http=True,
            )

    @OrderedStep('Opening URL in browser window.')
    def open_in_browser_window(self):
        '''
        Object Permissions
        ------------------

        Object access is governed by a set of permissions on that object.
        These "ACLs" can be applied after the object has been created. The
        default ACL for objects is private, meaning that we won't be able to
        actually access the object via its public URL.

        Let's open the URL in a web browser to illustrate that point.
        '''

        webbrowser.open_new(self.public_url)

    @OrderedStep('Generating a signed URL for the object')
    def generate_signed_url(self):
        '''
        Signed URLs
        -----------

        One way to grant access to an object that isn't publicly readable
        is to generate a "signed" URL that expires after a certain period
        of time. Let's generate one for our object.
        '''

        self.signed_url = self.key.generate_url(
            expires_in=3600,
            query_auth=True,
            force_http=True,
            )

    @OrderedStep('Opening signed URL in browser window')
    def open_signed_in_browser(self):
        '''
        Viewing Signed URLs
        -------------------

        Let's illustrate that our signed URL grants us access to our object
        by viewing it in a web browser.

           Signed Url: {signed_url}
        '''

        webbrowser.open_new(self.signed_url)

    @OrderedStep('Setting permissions to "public-read" on object')
    def set_permissions(self):
        '''
        Setting Object Permissions
        --------------------------

        DreamObjects supports the full spectrum of S3-like ACLs, including
        some "canned" ACLs that provide commonly used permissions. Let's mark
        our object with the "public-read" canned ACL.
        '''

        self.key.set_canned_acl('public-read')

    @OrderedStep('Viewing object in browser')
    def view_in_browser(self):
        '''
        Let's prove that we've successfully set the ACL by opening the
        public URL for the object in a browser again. This time, we should
        see the DreamHost logo load.
        '''

        webbrowser.open_new(self.public_url)

    @OrderedStep('Deleting bucket')
    def delete_bucket_fail(self):
        '''
        Deleting Buckets and Objects
        ----------------------------

        DreamObjects supports deleting both objects and buckets via the S3 API.
        Let's try and delete our bucket.
        '''

        try:
            self.conn.delete_bucket(self.bucket_name)
        except: # pylint: disable=bare-except
            print('   -> The bucket could not be deleted because ' +
                  '      it still contains an object!')

    @OrderedStep('Deleting object')
    def delete_object(self):
        '''
        Let's delete the object in the bucket, so that we can then delete
        the bucket.
        '''

        self.bucket.delete_key(self.object_name)

    @OrderedStep('Re-opening object URL')
    def re_open_url(self):
        '''
        Let's prove that the object is gone by trying to view it in our
        browser.
        '''
        webbrowser.open_new(self.public_url)

    @OrderedStep('Deleting bucket')
    def delete_bucket(self):
        '''Finally, let's clean up after ourselves and delete the bucket.'''
        self.conn.delete_bucket(self.bucket_name)

    @OrderedStep('Re-opening object URL (again)')
    def re_open_url_again(self):
        '''
        Let's prove that the bucket is gone by trying to view it in our
        browser.
        '''
        webbrowser.open_new(self.public_url)

    @staticmethod
    def _prompt():
        print
        raw_input('Press ENTER to continue...')
        print

    @staticmethod
    def _print(string, style='title'):
        color = {
            'title': 'yellow',
            'success': 'green',
            'failure': 'red',
            'header': 'cyan',
            }.get(style, 'white')

        attrs = ['bold'] if style == 'title' else []
        print colored(string, color, attrs=attrs)

    def _print_doc(self, docstring):
        if docstring is None:
            return

        self._print(cleandoc(docstring).format(
            access_key=self.access_key,
            secret_key=self.secret_key,
            bucket_name=self.bucket_name,
            object_name=self.object_name,
            public_url=self.public_url,
            signed_url=self.signed_url,
            ), style='header')

    def run(self):
        '''
        Run the demo steps, in order.
        '''
        for step_method in OrderedStep.steps:
            # print out any introduction to this section
            self._print_doc(step_method.__doc__)

            # now, ask to continue
            if step_method.prompt:
                self._prompt()

            # print the title
            if step_method.title:
                self._print(step_method.title + '...')

            # call the method
            try:
                step_method(self)
            except:
                # print the success message
                if step_method.title:
                    self._print('  -> failure!', style='failure')
                    print

                # re-raise the exception
                raise
            else:
                # print the success message
                if step_method.title:
                    self._print('  -> success!', style='success')
                    print


def main():
    '''
    DreamObjects Demo App
    '''
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        '--access-key',
        action='store',
        dest='access_key',
        help='DreamObjects S3 Access Key',
        required=True,
        )
    parser.add_argument(
        '--secret-key',
        action='store',
        dest='secret_key',
        help='DreamObjects S3 Secret Key',
        required=True,
        )
    parser.add_argument(
        '--use-s3',
        action='store_true',
        dest='use_s3',
        default=False,
        help='Use S3 rather than DreamObjects',
        )

    args = parser.parse_args()

    DreamObjectsDemo(
        access_key=args.access_key,
        secret_key=args.secret_key,
        bucket_name=str(uuid()),
        object_name='dreamhost-logo.png',
        use_s3=args.use_s3,
        show_http_traffic=True,
        ).run()

if __name__ == '__main__':
    main()

