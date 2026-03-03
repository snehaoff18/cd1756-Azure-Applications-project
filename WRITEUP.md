# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

Deployment Analysis: VM vs App Service for FlaskWebProject (CMS App)
# Option 1: Virtual Machine (VM)
*Cost Analysis*

You pay for:

VM compute (CPU + RAM)

OS disk

Networking

Public IP

Charges continue even if the app is idle

Requires manual scaling (adding new VMs increases cost significantly)

*Cost Level: Medium to High (for small web apps)*

*Scalability*

Manual scaling (vertical or horizontal)

Need to:

Configure load balancer

Set up multiple VMs

Handle traffic distribution manually

No built-in auto-scale unless configured separately

More operational effort required.

*Availability*

Must configure:

Availability Sets or Availability Zones

Health monitoring

Single VM = single point of failure

Risky unless high-availability architecture is manually implemented.

*Workflow & Management*

Full control over OS and environment

Need to:

Install Python, Flask, Gunicorn, Nginx

Configure reverse proxy

Manage security patches

Handle updates and backups

DevOps overhead is high

More infrastructure management required.

 # Option 2: Azure App Service (Chosen Solution)*
*Cost Analysis*

Pay only for selected App Service Plan tier

No OS management cost

Free and Basic tiers available

Built-in scaling reduces operational overhead

Cost Level: Low to Medium (ideal for small-to-medium web apps)

*Scalability*

Built-in auto-scaling

Easy vertical scaling (change pricing tier)

Easy horizontal scaling (increase instance count)

No load balancer setup required

Excellent for growing CMS traffic.

*Availability*

Built-in high availability

SLA-backed service (depending on tier)

Automatic health monitoring

Managed platform reduces downtime risks

Better reliability for production apps.

*Workflow & Management*

Platform as a Service (PaaS)

No need to manage:

OS updates

Security patching

Server configuration

*Supports:*

GitHub deployment

Azure DevOps

Zip deploy

CI/CD pipelines

Native support for Python/Flask

Faster deployment and easier maintenance.


### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
*Final Decision: Azure App Service*

I chose Azure App Service for deploying the FlaskWebProject CMS application.

*Justification*

Azure App Service is more suitable because:

The CMS app is a web-based Flask application

It does not require:

Custom OS-level configurations

Special networking setups

It benefits from:

Built-in scaling

Managed infrastructure

Faster deployment workflow

Lower operational complexity compared to managing a VM

Since this is a standard web app with SQL database and Blob Storage integration, App Service provides all required capabilities without infrastructure management overhead.

Therefore, App Service provides:

Better scalability

Lower management effort

Higher availability

More cost efficiency for this use case

When Would a VM Be a Better Choice?

I would reconsider using a Virtual Machine if:

The application required:

Custom system-level software

Special Linux modules

Deep OS configuration

Custom firewall rules not supported in App Service

The app required:

Background services running continuously

Custom networking configurations

Self-hosted services like:

Custom message brokers

Special database engines

Non-supported runtimes

Enterprise-level control requirements:

Strict OS compliance policies

Custom security hardening

Full control over server environment

*What Changes Would Make Me Switch to a VM?*

To justify switching to a VM, the CMS app would need:

Custom server software installed at OS level

Advanced reverse proxy configurations beyond App Service capabilities

Tight integration with internal network infrastructure

Highly customized deployment pipelines requiring root-level access

Hosting multiple tightly coupled services on the same server

In such cases, the flexibility of a VM would outweigh the operational simplicity of App Service.


Therefore, Azure App Service is the appropriate deployment choice for this project.