#!perl

use strict;
use Config::File;
use Pod::Usage;
use Getopt::Long qw(:config bundling auto_version auto_help);
$main::VERSION = 1.0;		# Define version of current script

my $string;
my $number;
my $switch;
my $cumulative;
my $config_file;
my $config_hash;

GetOptions(
	"s|string=s" => \$string,
	"n|number=i" => \$number,
	"w|switch"  => \$switch,
	"c|cumulative+" => \$cumulative,
	"f|file_configuration=s" => \$config_file;
);

$config_hash = Config::File::read_config_file($config_file) unless (-e $config_file);

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

commandline.pl [-s string] [-n num] [-w] [-c|-cc]

Options:
    -s, --string    String option
    -n, --number    Number option
    -w, --switch    Switch setting
    -c, -cc         Cumulative option

=head1 Author

Julio Molina Soler <j.molina@telenet.be>

=cut
