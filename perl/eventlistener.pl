#!/usr/bin/env perl

use strict;
use EV;
use Config::File;
use Pod::Usage;
use Log::Log4perl qw(:levels);
use Log::Log4perl::CommandLine ':all',
    ':loginit' => [{level => $INFO,
		    layout => '%d{ISO8601} [%p] [%F{1}:%L] %m%n'}];
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
	"f|file_configuration=s" => \$config_file,
);

$config_hash = Config::File::read_config_file($config_file) if(-e $config_file);

pod2usage({
	-message => q{Missing string value},
	-exitval => 1,
	-verbose => 1
	}) unless ($string);

my $logger = Log::Log4perl->get_logger();

# Register the events and the rutines in case it happens
my $event_timer = EV::timer 2, 2, sub {
    $logger->info("is called roughly every 2s (repeat = 2)");
};

my $event_io = EV::io *STDIN, EV::READ, sub {
    my ($w, $revents) = @_; # all callbacks receive the watcher and event mask
    $logger->info("stdin is readable, you entered: ", <STDIN>);
};

my $event_signal = EV::signal 'QUIT', sub {
    $logger->info("sigquit received");
};

my $event_filechange = EV::stat "/etc/passwd", 10, sub {
    my ($w, $revents) = @_;
    $logger->info($w->path, " has changed somehow.");
};

# Main loop, where the magic comes
EV::run;

__END__

=head1 NAME

eventlistener: template for event listener

=head1 SYNOPSYS

eventlistener.pl -h

Options:
	
    -d, --debug     Show debug level
    -v, --verbose   Show info level
    -q, --quiet     Supress all log information
    -s, --string    String option
    -n, --number    Number option
    -w, --switch    Switch setting
    -c, -cc         Cumulative option

=head1 Author

Julio Molina Soler <j.molina@telenet.be>

=cut
