#!/usr/bin/perl

my $directory = '/MYDATA';

opendir(DIR,$directory);
my @files = readdir(DIR);
closedir(DIR);
foreach(@files){
  print $_,"\n";
}

