#!/usr/bin/env perl
use strict;
use Config::File;
use Pod::Usage;
use Log::Log4perl qw(:levels);
use Log::Log4perl::CommandLine ':all',
            ':loginit' => [{level => $INFO,
                            layout => '%d{yyyy-MM-dd HH:mm:ss.SSS Z} [%p] [%F{1}:%L] %m%n'}];
use Getopt::Long qw(:config bundling auto_version auto_help);

$main::VERSION = 1.0; # Define version of current script

my $string;
my $number;
my $switch;
my $cumulative;
my $config_file;
my $config_hash;
my $daemonize;

GetOptions("s|string=s" => \$string,
          "n|number=i" => \$number,
          "w|switch" => \$switch,
          "c|cumulative+" => \$cumulative,
          "f|file_configuration=s" => \$config_file,
          );
          
$config_hash = Config::File::read_config_file($config_file) if(-e $config_file);

if($daemonize){
  require Proc::Daemon;
  my $file_log = Log::Log4perl::Appender->new('Log::Dispatch::FileRotate',
                                              name => 'fileRotation',
                                              filename => 'output.log',
                                              mode => 'append',
                                              DatePattern => 'yyyy-MM-dd');
  my $layout = Log::Log4perl::Layout::PatternLayout->new(
                                                         "%d{yyyy-MM-dd HH:mm:ss.SSS Z} [%p] [%F{1}:%L] %m%n");
  $file_log->layout($layout);
  $logger->add_appender($file_log);
  
  Proc::Daemon::Init;
}

pod2usage({
          -message => q{Missing string value},
          -exitval => 1,
          -verbose => 1
          }) unless ($string);
          
# Init the logger
my $logger = Log::Log4perl->get_logger();

# The main code here
$logger->info("Starting $0");
...
$logger->info("End $0");

__END__
=head1 NAME
commandline: template for creating command line with perl scripts
=head1 SYNOPSYS
Add here the information that would show the help
commandline.pl [-s string] [-n num] [-w] [-c|-cc] [-d|-v|-q]
Options:
-d, --debug Show debug level
-v, --verbose Show info level
-q, --quiet Supress all log information
-s, --string String option
-n, --number Number option
-w, --switch Switch setting
-c, -cc Cumulative option
=head1 Author
Julio Molina Soler <j.molina@telenet.be>
=cut
