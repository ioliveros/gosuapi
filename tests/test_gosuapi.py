import pytest

from gosuapi import headlines, matches, rankings, hero_statistics, events    

def test_headlines():
	assert headlines() == True

def test_matches():
	assert matches() == False

def test_rankings():
	assert rankings() == True

def test_herostatistics():
	assert hero_statistics() == True

def test_events():
	assert events() == True
