#!/bin/bash 
#
# This bash script aims to update the password of all remote machines listed. 
# The **new password** is hereby stored in a separate file called:
# - **updatedPW** and should contain the new password in a single line 
# The **old password** ought to be stored in a separated file as well:
# - **oldPW** and should contain the old password to connect with 
#
# ---
# -- adding and traversing all hosts 
#
# In order to traverse every machine and update their password
# we require a _**list**_ of those that should contain the following:
# - IP-Address 
# - username -> netz-ak for most | netzak for some
# - maybe type --> changing password may differ amongst the machines 
#
# **Those information are stored within "hosts"**
# Each _line_ contains the following information in the given structure:
# username:ipAddress:switchType
#
# example: netzak:10.251.0.0:OS6250


# ==== ==== ==== ====
# = actual script =
# ==== ==== ==== ==== 

# function that takes a string of type "Parameter1:Parameter2..." and
# returns its content as array 
# where ":" is the splitting character 
function stripString () {
		# taking *reference to array given as parameter*
		local -n array=$1
		# IFS contains information on special values that Strings are split up with 
		# we add : as separator here
		IFS=":" read -r -a array <<< $2
}

# --- / 
# -- / extracting host information from file 
#
BundledHosts=$(<hosts)

# --- / 
# -- / extracting **old password** and **new password**
# TODO Finde secure method to import those information /
# old_password=$(<oldPassword)
new_password=$(<newPassword)

# --- / 
# -- / setting script to execute **inside SSH-Connection
# this also differs from machine to machine ! 

command_afterUpdate="echo 'update complete, leaving'"
SCRIPT="echo '${new_password}; ${command_afterUpdate}' "
# SCRIPT="uname -r"

# --- / 
# -- / 
# - / iterating over all hosts extracted
function iterateSshOnMachines {
		# iterating over each line of hosts
		for BUNDLE in ${BundledHosts}; do 
			# declaring array to be filled with host information
			local arrayHostInformation 
			stripString arrayHostInformation ${BUNDLE}
			# executing SSH connection and running script
			# echo " ${arrayHostInformation[0]}@${arrayHostInformation[1]} "
			echo " ${arrayHostInformation[2]}"
			sshpass -f oldPassword ssh -o StrictHostKeyChecking=no -l ${arrayHostInformation[0]}  ${arrayHostInformation[1]} -t ${SCRIPT}
			# ${SCRIPT}
			# ${command_afterUpdate}

			# TODO requires fail safe to abort timeout behavior
		done 
}
# executing script 
cat overview.txt 
echo " Running script; updating all passwords accordingly."
iterateSshOnMachines 

