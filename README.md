# env-bootstrap
Deploy your infrastructure from scratch

## Notes/howtos/tips

### Tip: create env on Windows Desktop Docker

Q: Error "Could not open a connection to your authentication agent"
A: run following commands from GitBash prompt
- [ ]  `ssh-keygen` # generates ~/.ssh/id_rsa (private key) and ~/.ssh/id_rsa.pub
- [ ]  `eval $(ssh-agent -s)` # initializes SSH Agent
- [ ]  `ssh-add ~/.ssh/id_rsa` # adds private key to the agent


