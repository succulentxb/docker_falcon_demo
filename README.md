### Falcon Docker Demo

#### image build
When in current work directory, run cmd:  
`docker build --tag falcon_demo .`

#### image run
After image built, run cmd:  
`docker run -d -p 8080:80 falcon_demo`