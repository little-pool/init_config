# -*- mode: python; python-indent: 4 -*-
import ncs
from tools.get_linkaddress import get_linkaddress
from ncs.application import Service
from IPy import IP


# ------------------------
# SERVICE CALLBACK EXAMPLE
# ------------------------
class link_service_ServiceCallbacks(Service):
    
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info('Service create(service=', service._path, ')')
        print('link_service is running')
        part_name = service.part_name
        netblock = service.netblock
        netaddress = IP(netblock.netaddress+'/'+netblock.netmask)
        links = service.link
        print(type(links))
        print(len(links))
        linkipgen = get_linkaddress(netaddress)
        print(linkipgen.__next__())
        print(linkipgen.__next__())
        print(linkipgen.__next__())
            
        
        
        
        

    @Service.pre_modification
    def cb_pre_modification(self, tctx, op, kp, root, proplist):
        self.log.info('Service premod(service=', kp, ')')

    @Service.post_modification
    def cb_post_modification(self, tctx, op, kp, root, proplist):
        self.log.info('Service premod(service=', kp, ')')

class IGP_service_ServiceCallbacks(Service):
    
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info('Service create(service=', service._path, ')')
        print('IGP_service is running')

    @Service.pre_modification
    def cb_pre_modification(self, tctx, op, kp, root, proplist):
        self.log.info('Service premod(service=', kp, ')')

    @Service.post_modification
    def cb_post_modification(self, tctx, op, kp, root, proplist):
        self.log.info('Service premod(service=', kp, ')')


# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        # The application class sets up logging for us. It is accessible
        # through 'self.log' and is a ncs.log.Log instance.
        self.log.info('Main RUNNING')

        # Service callbacks require a registration for a 'service point',
        # as specified in the corresponding data model.
        #
        #self.register_service('init_config-servicepoint', ServiceCallbacks)
        self.register_service('link_service-servicepoint', link_service_ServiceCallbacks)
        self.register_service('IGP_service-servicepoint', IGP_service_ServiceCallbacks)

        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
