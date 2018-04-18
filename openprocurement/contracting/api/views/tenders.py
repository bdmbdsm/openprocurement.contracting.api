# -*- coding: utf-8 -*-
from hashlib import sha512
from openprocurement.api.utils import (
    json_view,
    APIResource,
)

from openprocurement.auctions.core.utils import opresource


@opresource(name='Auction credentials',
            path='/auctions/{tender_id}/extract_credentials',
            description="Open Contracting compatible data exchange format. See http://ocds.open-contracting.org/standard/r/master/#tender for more info")
class TenderResource(APIResource):

    @json_view(permission='extract_credentials')
    def get(self):
        self.LOGGER.info('Extract credentials for tender {}'.format(self.context.id))
        tender = self.request.validated['tender']
        data = tender.serialize('contracting')
        data['tender_token'] = sha512(tender.owner_token).hexdigest()
        return {'data': data}
