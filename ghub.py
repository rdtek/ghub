import requests
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

github_user = 'rdtek'

num_args = len(sys.argv)
if(num_args >= 2):
	github_user = sys.argv[1]

req_url = 'https://api.github.com/users/' + github_user + '/repos'
#print( req_url )

req = requests.get( req_url )

resp_json = req.json();

print( 'Repository list for user: ' + github_user )

for repo in resp_json:
	print( '\n ' + repo['name'] )
