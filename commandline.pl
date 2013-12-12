#!perl

use strict;
use Pod::Usage;
use Getopt::Long qw(:config bundling auto_version auto_help);
$main::VERSION = 1.0;		# Define version of current script

my $string;
my $number;
my $switch;
my $cumulative;

GetOptions(
	"s|string=s" => \$string,
	"n|number=i" => \$number,
	"w|switch"  => \$switch,
	"c|cumulative+" => \$cumulative
);

pod2usage({
	-message => q{Missing string value},
	-exitval => 1,
	-verbose => 1
	}) unless ($string);

# The main code here

__END__

=head1 NAME

commandline: template for creating command line with perl scripts

=head1 SYNOPSYS

Add here the information that would show the help

=cut
