import subprocess


class DockerCreator:


    def run_jenkins_agent(self):
        return subprocess.run("docker run -d --rm --name jenkins_agent -p 4444:22 -e 'JENKINS_AGENT_SSH_PUBKEY=ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC+SvhT/9mESmoiQUJRKEDd5/GhaLuYJQE9NFhOlr21bdUUv17Ms7FZ/JAthkBF7m1hyLcSz82UU9NHfByiKSEcSXs7iXUIBBy/irBnd5TdT4RsyDqGExtqOelnkK4+Ru1lm+D1JOLwSryzcY1+633e73qEiUUPVeRMDEB3ytoeR7D1HVnh6po57UHfAo3Pw2ZvPIXhaXl1lWk5Wb6qwdPPBcgxmJx+rGfwf59gWH7HHO62xnAfhlDMFPIRuQvt24JnZvba1ukuKCjVcro0d6ycTieMplkRKhQNGKqmX7HH1ypZO4PPMym8arbAh2c2yydVtYq5BH/nY+abe9u2apyUKe692/MS5qEfEu5yWiKs8TDV0xIkls+dFIp1gNpye3PncQe3/rATRr0vk/Ms1ap4pNkWaASym2pl5m4Emvzkk+XRgR6d+5PadKtn5FsTnv1EhyvDjEH4u9llRv1sb5sn6xR5gmYE5OaIJwV2xwAzfZM9VCEvW3kW6AncX/NE/Uc= al@fedora' jenkins/ssh-agent", shell=True, capture_output=True)


    def run_nginx_docker(self):
        return subprocess.run("docker run -d --rm -p 80:80 --name nginx_test nginx", shell=True, capture_output=True)
