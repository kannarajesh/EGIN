#!/usr/bin/perl

local ($buffer, @pairs, $pair, $name, $value, %FORM);
# Read in text
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

if ($ENV{'REQUEST_METHOD'} eq "POST") {
   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
} else {
   $buffer = $ENV{'QUERY_STRING'};
}

# Split information into name/value pairs
@pairs = split(/&/, $buffer);

foreach $pair (@pairs) {
   ($name, $value) = split(/=/, $pair);
   $value =~ tr/+/ /;
   $value =~ s/%(..)/pack("C", hex($1))/eg;
   $FORM{$name} = $value;
}
$opt = $FORM{opt};
$searchd = $FORM{searchd};

if ($opt eq "SOP")
{
$i=`ls -lrth /MYDATA/SOP/$searchd |wc -l`;
for( $a = 0; $a < $i; $a = $a + 1 ) 
{
$out = (`ls /MYDATA/SOP/$searchd`)[$a];
push(@val,"<br> $out <br>");
}
}
else
{
$r = `ls -lrth /MYDATA/INV/$searchd |wc -l`;
for( $q = 0; $q < $r; $q = $q + 1 ) 
{
$out1= (`ls /MYDATA/INV/$searchd`)[$q];
push(@val,"<br> $out1 <br>");
}

}

$sleep='sleep 20';
print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print "<title>Welcome To EIGN</title>";
print "</head>";
print "<body>";
print "<h2>Your result in $opt</h2>";
print "@val";
print "</body>";
print "</html>";

1;
