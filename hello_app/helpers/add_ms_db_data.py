from hello_app.helpers.ms_db import User, db, TenantSku

student_john = TenantSku(
    sku_name='Windows 365 W3',
    sku_guid='that-long-ass-guid',

    tenant_name='Pixel',
    tenant_guid='some-long-ass-guid',

    consumed=2,
    warning=0,
    enabled=2,
    suspended=1,

    active=True
)
sammy = TenantSku(
    sku_name='Microsoft 365 Busy',
    sku_guid='this-long-ass-guid',

    tenant_name='Pixel',
    tenant_guid='some-long-ass-guid',

    consumed=2,
    warning=0,
    enabled=2,
    suspended=1,

    active=True
)
carl = User(
    tenant_name='Pixel',
    tenant_guid='some-long-ass-guid',

    displayname='Carl',
    sku_names='Microsoft 365 Busy',

    email='carlwhite@example.com',
    active=True,
)
timma = User(
    tenant_name='Pixel',
    tenant_guid='some-long-ass-guid',

    displayname='timma',
    sku_names='Windows 365 W3',

    email='timma@example.com',
    active=True,
)

db.session.add(sammy)
db.session.add(carl)
db.session.add(student_john)
db.session.add(timma)
db.session.commit()
