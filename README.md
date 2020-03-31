<h1> Mac_Changer </h1>

<p>Progam in python to change MAC address</p>

<h2>Used Modules</h2>

<ul>
  <li>subprocess</li>
  <li>optparse</li>
  <li>re</li>
</ul>

<h3>Subprocess</h3>

<p>The module is used to perform the commands from the progam, so with the code lines below you can perform commands on the terminal.</p>

```python
subprocess.call(["sudo", "ifconfig", interface,  "down"])
subprocess.call(["sudo", "ifconfig", interface,  "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])
```

<h3>Optparse</h3>

<p>The module allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages</p>

```python
parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface", help="interface to change the MAC")
parser.add_option("-m","--mac",dest="mac",help="the new MAC address")
(options, arguments) = parser.parse_args()
Therefore you can now use like that: 
```

<h3>re</h3>

<p>This module provides regular expression matching operations, you can filter the content by looking for the MAC address in the result of the command "ifconfig"</p>

<p>The method check_output return the content of "ifconfig", and "re.search" look for somenthing that have a sequence of alpha numerics, using "\w" like argument in the method search</p>

```python
ifconfig_result = subprocess.check_output(["sudo", "ifconfig", interface])
mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result

if mac_search_result:
return mac_search_result.group(0)
else:
print("Couldn't read the MAC address")
```






