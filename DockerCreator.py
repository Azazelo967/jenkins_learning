import subprocess


class DockerCreator:


    def run_jenkins_agent(self):
        with open("/home/al/.ssh/jenkins_keys/id_rsa.pub", "r") as key_file:
            ssh_key = key_file.readline()
        subprocess.run("echo ssh key is " + ssh_key, shell=True)
        return subprocess.run("docker run -d --rm --name jenkins_agent -p 4444:22 -e 'JENKINS_AGENT_SSH_PUBKEY=" + ssh_key, shell=True, capture_output=True)


    def run_nginx_docker(self):
        return subprocess.run("docker run -d --rm -p 80:80 --name nginx_test nginx", shell=True, capture_output=True)
