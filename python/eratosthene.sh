#!/bin/bash
# argument : limite supérieure pour la recherche de nombres entiers.

UPPER_LIMIT=$1                  # argument du script, la limite supérieure
let SPLIT=UPPER_LIMIT/2         
# optimisation la moitié (entière) du nombre fourni : pas de calculs en virgule flottante possibles en shell bash, racine carrée on 
# oublie... sauf à utiliser bc

Primes=( '' $(seq $UPPER_LIMIT) )

i=1
until (( ( i += 1 ) > SPLIT ))  
# Optimisation du crible : la recherche s’effectue sur la moitie de l’intervalle initial.
do
  if [[ -n ${Primes[i]} ]]
  then
    t=$i
    until (( ( t += i ) > UPPER_LIMIT ))
    do
      Primes[t]=
    done
  fi  
done  
echo ${Primes[*]}

exit $?