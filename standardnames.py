## http://www.unix.org/version3/apis.html
## more standards to follow

functionnames = [ 'FD_CLR'
                , 'FD_ISSET'
                , 'FD_SET'
                , 'FD_ZERO'
                , '_Exit'
                , '_exit'
                , '_longjmp'
                , '_setjmp'
                , '_tolower'
                , '_toupper'
                , 'a64l'
                , 'abort'
                , 'abs'
                , 'accept'
                , 'access'
                , 'acos'
                , 'acosf'
                , 'acosh'
                , 'acoshf'
                , 'acoshl'
                , 'acosl'
                , 'aio_cancel'
                , 'aio_error'
                , 'aio_fsync'
                , 'aio_read'
                , 'aio_return'
                , 'aio_suspend'
                , 'aio_write'
                , 'alarm'
                , 'asctime'
                , 'asctime_r'
                , 'asin'
                , 'asinf'
                , 'asinh'
                , 'asinhf'
                , 'asinhl'
                , 'asinl'
                , 'assert'
                , 'atan'
                , 'atan2'
                , 'atan2f'
                , 'atan2l'
                , 'atanf'
                , 'atanh'
                , 'atanhf'
                , 'atanhl'
                , 'atanl'
                , 'atexit'
                , 'atof'
                , 'atoi'
                , 'atol'
                , 'atoll'
                , 'basename'
                , 'bcmp'
                , 'bcopy'
                , 'bind'
                , 'bsd_signal'
                , 'bsearch'
                , 'btowc'
                , 'bzero'
                , 'cabs'
                , 'cabsf'
                , 'cabsl'
                , 'cacos'
                , 'cacosf'
                , 'cacosh'
                , 'cacoshf'
                , 'cacoshl'
                , 'cacosl'
                , 'calloc'
                , 'carg'
                , 'cargf'
                , 'cargl'
                , 'casin'
                , 'casinf'
                , 'casinh'
                , 'casinhf'
                , 'casinhl'
                , 'casinl'
                , 'catan'
                , 'catanf'
                , 'catanh'
                , 'catanhf'
                , 'catanhl'
                , 'catanl'
                , 'catclose'
                , 'catgets'
                , 'catopen'
                , 'cbrt'
                , 'cbrtf'
                , 'cbrtl'
                , 'ccos'
                , 'ccosf'
                , 'ccosh'
                , 'ccoshf'
                , 'ccoshl'
                , 'ccosl'
                , 'ceil'
                , 'ceilf'
                , 'ceill'
                , 'cexp'
                , 'cexpf'
                , 'cexpl'
                , 'cfgetispeed'
                , 'cfgetospeed'
                , 'cfsetispeed'
                , 'cfsetospeed'
                , 'chdir'
                , 'chmod'
                , 'chown'
                , 'cimag'
                , 'cimagf'
                , 'cimagl'
                , 'clearerr'
                , 'clock'
                , 'clock_getcpuclockid'
                , 'clock_getres'
                , 'clock_gettime'
                , 'clock_nanosleep'
                , 'clock_settime'
                , 'clog'
                , 'clogf'
                , 'clogl'
                , 'close'
                , 'closedir'
                , 'closelog'
                , 'confstr'
                , 'conj'
                , 'conjf'
                , 'conjl'
                , 'connect'
                , 'copysign'
                , 'copysignf'
                , 'copysignl'
                , 'cos'
                , 'cosf'
                , 'cosh'
                , 'coshf'
                , 'coshl'
                , 'cosl'
                , 'cpow'
                , 'cpowf'
                , 'cpowl'
                , 'cproj'
                , 'cprojf'
                , 'cprojl'
                , 'creal'
                , 'crealf'
                , 'creall'
                , 'creat'
                , 'crypt'
                , 'csin'
                , 'csinf'
                , 'csinh'
                , 'csinhf'
                , 'csinhl'
                , 'csinl'
                , 'csqrt'
                , 'csqrtf'
                , 'csqrtl'
                , 'ctan'
                , 'ctanf'
                , 'ctanh'
                , 'ctanhf'
                , 'ctanhl'
                , 'ctanl'
                , 'ctermid'
                , 'ctime'
                , 'ctime_r' 
                , 'daylight'
                , 'dbm_clearerr'
                , 'dbm_close'
                , 'dbm_delete'
                , 'dbm_error'
                , 'dbm_fetch'
                , 'dbm_firstkey'
                , 'dbm_nextkey'
                , 'dbm_open'
                , 'dbm_store'
                , 'difftime'
                , 'dirname'
                , 'div'
                , 'dlclose'
                , 'dlerror'
                , 'dlopen'
                , 'dlsym'
                , 'drand48'
                , 'dup'
                , 'dup2'
                , 'ecvt'
                , 'encrypt'
                , 'endgrent'
                , 'endhostent'
                , 'endnetent'
                , 'endprotoent'
                , 'endpwent'
                , 'endservent'
                , 'endutxent'
                , 'environ'
                , 'erand48'
                , 'erf'
                , 'erfc'
                , 'erfcf'
                , 'erfcl'
                , 'erff'
                , 'erfl'
                , 'errno'
                , 'execl'
                , 'execle'
                , 'execlp'
                , 'execv'
                , 'execve'
                , 'execvp'
                , 'exit'
                , 'exp'
                , 'exp2'
                , 'exp2f'
                , 'exp2l'
                , 'expf'
                , 'expl'
                , 'expm1'
                , 'expm1f'
                , 'expm1l'
                , 'fabs'
                , 'fabsf'
                , 'fabsl'
                , 'fattach'
                , 'fchdir'
                , 'fchmod'
                , 'fchown'
                , 'fclose'
                , 'fcntl'
                , 'fcvt'
                , 'fdatasync'
                , 'fdetach'
                , 'fdim'
                , 'fdimf'
                , 'fdiml'
                , 'fdopen'
                , 'feclearexcept'
                , 'fegetenv'
                , 'fegetexceptflag'
                , 'fegetround'
                , 'feholdexcept'
                , 'feof'
                , 'feraiseexcept'
                , 'ferror'
                , 'fesetenv'
                , 'fesetexceptflag'
                , 'fesetround'
                , 'fetestexcept'
                , 'feupdateenv'
                , 'fflush'
                , 'ffs'
                , 'fgetc'
                , 'fgetpos'
                , 'fgets'
                , 'fgetwc'
                , 'fgetws'
                , 'fileno'
                , 'flockfile'
                , 'floor'
                , 'floorf'
                , 'floorl'
                , 'fma'
                , 'fmaf'
                , 'fmal'
                , 'fmax'
                , 'fmaxf'
                , 'fmaxl'
                , 'fmin'
                , 'fminf'
                , 'fminl'
                , 'fmod'
                , 'fmodf'
                , 'fmodl'
                , 'fmtmsg'
                , 'fnmatch'
                , 'fopen'
                , 'fork'
                , 'fpathconf'
                , 'fpclassify'
                , 'fprintf'
                , 'fputc'
                , 'fputs'
                , 'fputwc'
                , 'fputws'
                , 'fread'
                , 'free'
                , 'freeaddrinfo'
                , 'freopen'
                , 'frexp'
                , 'frexpf'
                , 'frexpl'
                , 'fscanf'
                , 'fseek'
                , 'fseeko'
                , 'fsetpos'
                , 'fstat'
                , 'fstatvfs'
                , 'fsync'
                , 'ftell'
                , 'ftello'
                , 'ftime'
                , 'ftok'
                , 'ftruncate'
                , 'ftrylockfile'
                , 'ftw'
                , 'funlockfile'
                , 'fwide'
                , 'fwprintf'
                , 'fwrite'
                , 'fwscanf'
                , 'gai_strerror'
                , 'gcvt'
                , 'getaddrinfo'
                , 'getc'
                , 'getc_unlocked'
                , 'getchar'
                , 'getchar_unlocked'
                , 'getcontext'
                , 'getcwd'
                , 'getdate'
                , 'getegid'
                , 'getenv'
                , 'geteuid'
                , 'getgid'
                , 'getgrent'
                , 'getgrgid'
                , 'getgrgid_r'
                , 'getgrnam'
                , 'getgrnam_r'
                , 'getgroups'
                , 'gethostbyaddr'
                , 'gethostbyname'
                , 'gethostent'
                , 'gethostid'
                , 'gethostname'
                , 'getitimer'
                , 'getlogin'
                , 'getlogin_r'
                , 'getmsg'
                , 'getnameinfo'
                , 'getnetbyaddr'
                , 'getnetbyname'
                , 'getnetent'
                , 'getopt'
                , 'getpeername'
                , 'getpgid'
                , 'getpgrp'
                , 'getpid'
                , 'getpmsg'
                , 'getppid'
                , 'getpriority'
                , 'getprotobyname'
                , 'getprotobynumber'
                , 'getprotoent'
                , 'getpwent'
                , 'getpwnam'
                , 'getpwnam_r'
                , 'getpwuid'
                , 'getpwuid_r'
                , 'getrlimit'
                , 'getrusage'
                , 'gets'
                , 'getservbyname'
                , 'getservbyport'
                , 'getservent'
                , 'getsid'
                , 'getsockname'
                , 'getsockopt'
                , 'getsubopt'
                , 'gettimeofday'
                , 'getuid'
                , 'getutxent'
                , 'getutxid'
                , 'getutxline'
                , 'getwc'
                , 'getwchar'
                , 'getwd'
                , 'glob'
                , 'globfree'
                , 'gmtime'
                , 'gmtime_r'
                , 'grantpt'
                , 'h_errno'
                , 'hcreate'
                , 'hdestroy'
                , 'hsearch'
                , 'htonl'
                , 'htons'
                , 'hypot'
                , 'hypotf'
                , 'hypotl'
                , 'iconv'
                , 'iconv_close'
                , 'iconv_open'
                , 'if_freenameindex'
                , 'if_indextoname'
                , 'if_nameindex'
                , 'if_nametoindex'
                , 'ilogb'
                , 'ilogbf'
                , 'ilogbl'
                , 'imaxabs'
                , 'imaxdiv'
                , 'index'
                , 'inet_addr'
                , 'inet_ntoa'
                , 'inet_ntop'
                , 'inet_pton'
                , 'initstate'
                , 'insque'
                , 'ioctl'
                , 'isalnum'
                , 'isalpha'
                , 'isascii'
                , 'isastream'
                , 'isatty'
                , 'isblank'
                , 'iscntrl'
                , 'isdigit'
                , 'isfinite'
                , 'isgraph'
                , 'isgreater'
                , 'isgreaterequal'
                , 'isinf'
                , 'isless'
                , 'islessequal'
                , 'islessgreater'
                , 'islower'
                , 'isnan'
                , 'isnormal'
                , 'isprint'
                , 'ispunct'
                , 'isspace'
                , 'isunordered'
                , 'isupper'
                , 'iswalnum'
                , 'iswalpha'
                , 'iswblank'
                , 'iswcntrl'
                , 'iswctype'
                , 'iswdigit'
                , 'iswgraph'
                , 'iswlower'
                , 'iswprint'
                , 'iswpunct'
                , 'iswspace'
                , 'iswupper'
                , 'iswxdigit'
                , 'isxdigit'
                , 'j0'
                , 'j1'
                , 'jn'
                , 'jrand48'
                , 'kill'
                , 'killpg'
                , 'l64a'
                , 'labs'
                , 'lchown'
                , 'lcong48'
                , 'ldexp'
                , 'ldexpf'
                , 'ldexpl'
                , 'ldiv'
                , 'lfind'
                , 'lgamma'
                , 'lgammaf'
                , 'lgammal'
                , 'link'
                , 'lio_listio'
                , 'listen'
                , 'llabs'
                , 'lldiv'
                , 'llrint'
                , 'llrintf'
                , 'llrintl'
                , 'llround'
                , 'llroundf'
                , 'llroundl'
                , 'localeconv'
                , 'localtime'
                , 'localtime_r'
                , 'lockf'
                , 'log'
                , 'log10'
                , 'log10f'
                , 'log10l'
                , 'log1p'
                , 'log1pf'
                , 'log1pl'
                , 'log2'
                , 'log2f'
                , 'log2l'
                , 'logb'
                , 'logbf'
                , 'logbl'
                , 'logf'
                , 'logl'
                , 'longjmp'
                , 'lrand48'
                , 'lrint'
                , 'lrintf'
                , 'lrintl'
                , 'lround'
                , 'lroundf'
                , 'lroundl'
                , 'lsearch'
                , 'lseek'
                , 'lstat'
                , 'makecontext'
                , 'malloc'
                , 'mblen'
                , 'mbrlen'
                , 'mbrtowc'
                , 'mbsinit'
                , 'mbsrtowcs'
                , 'mbstowcs'
                , 'mbtowc'
                , 'memccpy'
                , 'memchr'
                , 'memcmp'
                , 'memcpy'
                , 'memmove'
                , 'memset'
                , 'mkdir'
                , 'mkfifo'
                , 'mknod'
                , 'mkstemp'
                , 'mktemp'
                , 'mktime'
                , 'mlock'
                , 'mlockall'
                , 'mmap'
                , 'modf'
                , 'modff'
                , 'modfl'
                , 'mprotect'
                , 'mq_close'
                , 'mq_getattr'
                , 'mq_notify'
                , 'mq_open'
                , 'mq_receive'
                , 'mq_send'
                , 'mq_setattr'
                , 'mq_timedreceive'
                , 'mq_timedsend'
                , 'mq_unlink'
                , 'mrand48'
                , 'msgctl'
                , 'msgget'
                , 'msgrcv'
                , 'msgsnd'
                , 'msync'
                , 'munlock'
                , 'munlockall'
                , 'munmap'
                , 'nan'
                , 'nanf'
                , 'nanl'
                , 'nanosleep'
                , 'nearbyint'
                , 'nearbyintf'
                , 'nearbyintl'
                , 'nextafter'
                , 'nextafterf'
                , 'nextafterl'
                , 'nexttoward'
                , 'nexttowardf'
                , 'nexttowardl'
                , 'nftw'
                , 'nice'
                , 'nl_langinfo'
                , 'nrand48'
                , 'ntohl'
                , 'ntohs'
                , 'open'
                , 'opendir'
                , 'openlog'
                , 'optarg'
                , 'opterr'
                , 'optind'
                , 'optopt'
                , 'pathconf'
                , 'pause'
                , 'pclose'
                , 'perror'
                , 'pipe'
                , 'poll'
                , 'popen'
                , 'posix_fadvise'
                , 'posix_fallocate'
                , 'posix_madvise'
                , 'posix_mem_offset'
                , 'posix_memalign'
                , 'posix_openpt'
                , 'posix_spawn'
                , 'posix_spawn_file_actions_addclose'
                , 'posix_spawn_file_actions_adddup2'
                , 'posix_spawn_file_actions_addopen'
                , 'posix_spawn_file_actions_destroy'
                , 'posix_spawn_file_actions_init'
                , 'posix_spawnattr_destroy'
                , 'posix_spawnattr_getflags'
                , 'posix_spawnattr_getpgroup'
                , 'posix_spawnattr_getschedparam'
                , 'posix_spawnattr_getschedpolicy'
                , 'posix_spawnattr_getsigdefault'
                , 'posix_spawnattr_getsigmask'
                , 'posix_spawnattr_init'
                , 'posix_spawnattr_setflags'
                , 'posix_spawnattr_setpgroup'
                , 'posix_spawnattr_setschedparam'
                , 'posix_spawnattr_setschedpolicy'
                , 'posix_spawnattr_setsigdefault'
                , 'posix_spawnattr_setsigmask'
                , 'posix_spawnp'
                , 'posix_trace_attr_destroy'
                , 'posix_trace_attr_getclockres'
                , 'posix_trace_attr_getcreatetime'
                , 'posix_trace_attr_getgenversion'
                , 'posix_trace_attr_getinherited'
                , 'posix_trace_attr_getlogfullpolicy'
                , 'posix_trace_attr_getlogsize'
                , 'posix_trace_attr_getmaxdatasize'
                , 'posix_trace_attr_getmaxsystemeventsize'
                , 'posix_trace_attr_getmaxusereventsize'
                , 'posix_trace_attr_getname'
                , 'posix_trace_attr_getstreamfullpolicy'
                , 'posix_trace_attr_getstreamsize'
                , 'posix_trace_attr_init'
                , 'posix_trace_attr_setinherited'
                , 'posix_trace_attr_setlogfullpolicy'
                , 'posix_trace_attr_setlogsize'
                , 'posix_trace_attr_setmaxdatasize'
                , 'posix_trace_attr_setname'
                , 'posix_trace_attr_setstreamfullpolicy'
                , 'posix_trace_attr_setstreamsize'
                , 'posix_trace_clear'
                , 'posix_trace_close'
                , 'posix_trace_create'
                , 'posix_trace_create_withlog'
                , 'posix_trace_event'
                , 'posix_trace_eventid_equal'
                , 'posix_trace_eventid_get_name'
                , 'posix_trace_eventid_open'
                , 'posix_trace_eventset_add'
                , 'posix_trace_eventset_del'
                , 'posix_trace_eventset_empty'
                , 'posix_trace_eventset_fill'
                , 'posix_trace_eventset_ismember'
                , 'posix_trace_eventtypelist_getnext_id'
                , 'posix_trace_eventtypelist_rewind'
                , 'posix_trace_flush'
                , 'posix_trace_get_attr'
                , 'posix_trace_get_filter'
                , 'posix_trace_get_status'
                , 'posix_trace_getnext_event'
                , 'posix_trace_open'
                , 'posix_trace_rewind'
                , 'posix_trace_set_filter'
                , 'posix_trace_shutdown'
                , 'posix_trace_start'
                , 'posix_trace_stop'
                , 'posix_trace_timedgetnext_event'
                , 'posix_trace_trid_eventid_open'
                , 'posix_trace_trygetnext_event'
                , 'posix_typed_mem_get_info'
                , 'posix_typed_mem_open'
                , 'pow'
                , 'powf'
                , 'powl'
                , 'pread'
                , 'printf'
                , 'pselect'
                , 'pthread_atfork'
                , 'pthread_attr_destroy'
                , 'pthread_attr_getdetachstate'
                , 'pthread_attr_getguardsize'
                , 'pthread_attr_getinheritsched'
                , 'pthread_attr_getschedparam'
                , 'pthread_attr_getschedpolicy'
                , 'pthread_attr_getscope'
                , 'pthread_attr_getstack'
                , 'pthread_attr_getstackaddr'
                , 'pthread_attr_getstacksize'
                , 'pthread_attr_init'
                , 'pthread_attr_setdetachstate'
                , 'pthread_attr_setguardsize'
                , 'pthread_attr_setinheritsched'
                , 'pthread_attr_setschedparam'
                , 'pthread_attr_setschedpolicy'
                , 'pthread_attr_setscope'
                , 'pthread_attr_setstack'
                , 'pthread_attr_setstackaddr'
                , 'pthread_attr_setstacksize'
                , 'pthread_barrier_destroy'
                , 'pthread_barrier_init'
                , 'pthread_barrier_wait'
                , 'pthread_barrierattr_destroy'
                , 'pthread_barrierattr_getpshared'
                , 'pthread_barrierattr_init'
                , 'pthread_barrierattr_setpshared'
                , 'pthread_cancel'
                , 'pthread_cleanup_pop'
                , 'pthread_cleanup_push'
                , 'pthread_cond_broadcast'
                , 'pthread_cond_destroy'
                , 'pthread_cond_init'
                , 'pthread_cond_signal'
                , 'pthread_cond_timedwait'
                , 'pthread_cond_wait'
                , 'pthread_condattr_destroy'
                , 'pthread_condattr_getclock'
                , 'pthread_condattr_getpshared'
                , 'pthread_condattr_init'
                , 'pthread_condattr_setclock'
                , 'pthread_condattr_setpshared'
                , 'pthread_create'
                , 'pthread_detach'
                , 'pthread_equal'
                , 'pthread_exit'
                , 'pthread_getconcurrency'
                , 'pthread_getcpuclockid'
                , 'pthread_getschedparam'
                , 'pthread_getspecific'
                , 'pthread_join'
                , 'pthread_key_create'
                , 'pthread_key_delete'
                , 'pthread_kill'
                , 'pthread_mutex_destroy'
                , 'pthread_mutex_getprioceiling'
                , 'pthread_mutex_init'
                , 'pthread_mutex_lock'
                , 'pthread_mutex_setprioceiling'
                , 'pthread_mutex_timedlock'
                , 'pthread_mutex_trylock'
                , 'pthread_mutex_unlock'
                , 'pthread_mutexattr_destroy'
                , 'pthread_mutexattr_getprioceiling'
                , 'pthread_mutexattr_getprotocol'
                , 'pthread_mutexattr_getpshared'
                , 'pthread_mutexattr_gettype'
                , 'pthread_mutexattr_init'
                , 'pthread_mutexattr_setprioceiling'
                , 'pthread_mutexattr_setprotocol'
                , 'pthread_mutexattr_setpshared'
                , 'pthread_mutexattr_settype'
                , 'pthread_once'
                , 'pthread_rwlock_destroy'
                , 'pthread_rwlock_init'
                , 'pthread_rwlock_rdlock'
                , 'pthread_rwlock_timedrdlock'
                , 'pthread_rwlock_timedwrlock'
                , 'pthread_rwlock_tryrdlock'
                , 'pthread_rwlock_trywrlock'
                , 'pthread_rwlock_unlock'
                , 'pthread_rwlock_wrlock'
                , 'pthread_rwlockattr_destroy'
                , 'pthread_rwlockattr_getpshared'
                , 'pthread_rwlockattr_init'
                , 'pthread_rwlockattr_setpshared'
                , 'pthread_self'
                , 'pthread_setcancelstate'
                , 'pthread_setcanceltype'
                , 'pthread_setconcurrency'
                , 'pthread_setschedparam'
                , 'pthread_setschedprio'
                , 'pthread_setspecific'
                , 'pthread_sigmask'
                , 'pthread_spin_destroy'
                , 'pthread_spin_init'
                , 'pthread_spin_lock'
                , 'pthread_spin_trylock'
                , 'pthread_spin_unlock'
                , 'pthread_testcancel'
                , 'ptsname'
                , 'putc'
                , 'putc_unlocked'
                , 'putchar'
                , 'putchar_unlocked'
                , 'putenv'
                , 'putmsg'
                , 'putpmsg'
                , 'puts'
                , 'pututxline'
                , 'putwc'
                , 'putwchar'
                , 'pwrite'
                , 'qsort'
                , 'raise'
                , 'rand'
                , 'rand_r'
                , 'random'
                , 'read'
                , 'readdir'
                , 'readdir_r'
                , 'readlink'
                , 'readv'
                , 'realloc'
                , 'realpath'
                , 'recv'
                , 'recvfrom'
                , 'recvmsg'
                , 'regcomp'
                , 'regerror'
                , 'regexec'
                , 'regfree'
                , 'remainder'
                , 'remainderf'
                , 'remainderl'
                , 'remove'
                , 'remque'
                , 'remquo'
                , 'remquof'
                , 'remquol'
                , 'rename'
                , 'rewind'
                , 'rewinddir'
                , 'rindex'
                , 'rint'
                , 'rintf'
                , 'rintl'
                , 'rmdir'
                , 'round'
                , 'roundf'
                , 'roundl'
                , 'scalb'
                , 'scalbln'
                , 'scalblnf'
                , 'scalblnl'
                , 'scalbn'
                , 'scalbnf'
                , 'scalbnl'
                , 'scanf'
                , 'sched_get_priority_max'
                , 'sched_get_priority_min'
                , 'sched_getparam'
                , 'sched_getscheduler'
                , 'sched_rr_get_interval'
                , 'sched_setparam'
                , 'sched_setscheduler'
                , 'sched_yield'
                , 'seed48'
                , 'seekdir'
                , 'select'
                , 'sem_close'
                , 'sem_destroy'
                , 'sem_getvalue'
                , 'sem_init'
                , 'sem_open'
                , 'sem_post'
                , 'sem_timedwait'
                , 'sem_trywait'
                , 'sem_unlink'
                , 'sem_wait'
                , 'semctl'
                , 'semget'
                , 'semop'
                , 'send'
                , 'sendmsg'
                , 'sendto'
                , 'setbuf'
                , 'setcontext'
                , 'setegid'
                , 'setenv'
                , 'seteuid'
                , 'setgid'
                , 'setgrent'
                , 'sethostent'
                , 'setitimer'
                , 'setjmp'
                , 'setkey'
                , 'setlocale'
                , 'setlogmask'
                , 'setnetent'
                , 'setpgid'
                , 'setpgrp'
                , 'setpriority'
                , 'setprotoent'
                , 'setpwent'
                , 'setregid'
                , 'setreuid'
                , 'setrlimit'
                , 'setservent'
                , 'setsid'
                , 'setsockopt'
                , 'setstate'
                , 'setuid'
                , 'setutxent'
                , 'setvbuf'
                , 'shm_open'
                , 'shm_unlink'
                , 'shmat'
                , 'shmctl'
                , 'shmdt'
                , 'shmget'
                , 'shutdown'
                , 'sigaction'
                , 'sigaddset'
                , 'sigaltstack'
                , 'sigdelset'
                , 'sigemptyset'
                , 'sigfillset'
                , 'sighold'
                , 'sigignore'
                , 'siginterrupt'
                , 'sigismember'
                , 'siglongjmp'
                , 'signal'
                , 'signbit'
                , 'sigpause'
                , 'sigpending'
                , 'sigprocmask'
                , 'sigqueue'
                , 'sigrelse'
                , 'sigset'
                , 'sigsetjmp'
                , 'sigsuspend'
                , 'sigtimedwait'
                , 'sigwait'
                , 'sigwaitinfo'
                , 'sin'
                , 'sinf'
                , 'sinh'
                , 'sinhf'
                , 'sinhl'
                , 'sinl'
                , 'sleep'
                , 'snprintf'
                , 'sockatmark'
                , 'socket'
                , 'socketpair'
                , 'sprintf'
                , 'sqrt'
                , 'sqrtf'
                , 'sqrtl'
                , 'srand'
                , 'srand48'
                , 'srandom'
                , 'sscanf'
                , 'stat'
                , 'statvfs'
                , 'stderr'
                , 'stdin'
                , 'stdout'
                , 'strcasecmp'
                , 'strcat'
                , 'strchr'
                , 'strcmp'
                , 'strcoll'
                , 'strcpy'
                , 'strcspn'
                , 'strdup'
                , 'strerror'
                , 'strerror_r'
                , 'strfmon'
                , 'strftime'
                , 'strlen'
                , 'strncasecmp'
                , 'strncat'
                , 'strncmp'
                , 'strncpy'
                , 'strpbrk'
                , 'strptime'
                , 'strrchr'
                , 'strspn'
                , 'strstr'
                , 'strtod'
                , 'strtof'
                , 'strtoimax'
                , 'strtok'
                , 'strtok_r'
                , 'strtol'
                , 'strtold'
                , 'strtoll'
                , 'strtoul'
                , 'strtoull'
                , 'strtoumax'
                , 'strxfrm'
                , 'swab'
                , 'swapcontext'
                , 'swprintf'
                , 'swscanf'
                , 'symlink'
                , 'sync'
                , 'sysconf'
                , 'syslog'
                , 'system'
                , 'tan'
                , 'tanf'
                , 'tanh'
                , 'tanhf'
                , 'tanhl'
                , 'tanl'
                , 'tcdrain'
                , 'tcflow'
                , 'tcflush'
                , 'tcgetattr'
                , 'tcgetpgrp'
                , 'tcgetsid'
                , 'tcsendbreak'
                , 'tcsetattr'
                , 'tcsetpgrp'
                , 'tdelete'
                , 'telldir'
                , 'tempnam'
                , 'tfind'
                , 'tgamma'
                , 'tgammaf'
                , 'tgammal'
                , 'time'
                , 'timer_create'
                , 'timer_delete'
                , 'timer_getoverrun'
                , 'timer_gettime'
                , 'timer_settime'
                , 'times'
                , 'tmpfile'
                , 'tmpnam'
                , 'toascii'
                , 'tolower'
                , 'toupper'
                , 'towctrans'
                , 'towlower'
                , 'towupper'
                , 'trunc'
                , 'truncate'
                , 'truncf'
                , 'truncl'
                , 'tsearch'
                , 'ttyname'
                , 'ttyname_r'
                , 'twalk'
                , 'tzname'
                , 'tzset'
                , 'ualarm'
                , 'ulimit'
                , 'umask'
                , 'uname'
                , 'ungetc'
                , 'ungetwc'
                , 'unlink'
                , 'unlockpt'
                , 'unsetenv'
                , 'usleep'
                , 'utime'
                , 'utimes'
                , 'va_arg'
                , 'va_copy'
                , 'va_end'
                , 'va_start'
                , 'vfork'
                , 'vfprintf'
                , 'vfscanf'
                , 'vfwprintf'
                , 'vfwscanf'
                , 'vprintf'
                , 'vscanf'
                , 'vsnprintf'
                , 'vsprintf'
                , 'vsscanf'
                , 'vswprintf'
                , 'vswscanf'
                , 'vwprintf'
                , 'vwscanf'
                , 'wait'
                , 'waitid'
                , 'waitpid'
                , 'wcrtomb'
                , 'wcscat'
                , 'wcschr'
                , 'wcscmp'
                , 'wcscoll'
                , 'wcscpy'
                , 'wcscspn'
                , 'wcsftime'
                , 'wcslen'
                , 'wcsncat'
                , 'wcsncmp'
                , 'wcsncpy'
                , 'wcspbrk'
                , 'wcsrchr'
                , 'wcsrtombs'
                , 'wcsspn'
                , 'wcsstr'
                , 'wcstod'
                , 'wcstof'
                , 'wcstoimax'
                , 'wcstok'
                , 'wcstol'
                , 'wcstold'
                , 'wcstoll'
                , 'wcstombs'
                , 'wcstoul'
                , 'wcstoull'
                , 'wcstoumax'
                , 'wcswcs'
                , 'wcswidth'
                , 'wcsxfrm'
                , 'wctob'
                , 'wctomb'
                , 'wctrans'
                , 'wctype'
                , 'wcwidth'
                , 'wmemchr'
                , 'wmemcmp'
                , 'wmemcpy'
                , 'wmemmove'
                , 'wmemset'
                , 'wordexp'
                , 'wordfree'
                , 'wprintf'
                , 'write'
                , 'writev'
                , 'wscanf'
                , 'y0'
                , 'y1'
                , 'yn'
                ]

## errors defined in POSIX and others, from sysdeps/gnu/errlist.c in glibc
## TODO: add sysdeps/posix/gai_strerror-strs.h
errors = [
    "Success",
    "Operation not permitted",
    "No such file or directory",
    "No such process",
    "Interrupted system call",
    "Input/output error",
    "No such device or address",
    "Argument list too long",
    "Exec format error",
    "Bad file descriptor",
    "No child processes",
    "Resource deadlock avoided",
    "Cannot allocate memory",
    "Permission denied",
    "Bad address",
    "Block device required",
    "Device or resource busy",
    "File exists",
    "Invalid cross-device link",
    "No such device",
    "Not a directory",
    "Is a directory",
    "Invalid argument",
    "Too many open files",
    "Too many open files in system",
    "Inappropriate ioctl for device",
    "Text file busy",
    "File too large",
    "No space left on device",
    "Illegal seek",
    "Read-only file system",
    "Too many links",
    "Broken pipe",
    "Numerical argument out of domain",
    "Numerical result out of range",
    "Resource temporarily unavailable",
    "Operation would block",
    "Operation now in progress",
    "Operation already in progress",
    "Socket operation on non-socket",
    "Message too long",
    "Protocol wrong type for socket",
    "Protocol not available",
    "Protocol not supported",
    "Socket type not supported",
    "Operation not supported",
    "Protocol family not supported",
    "Address family not supported by protocol",
    "Address already in use",
    "Cannot assign requested address",
    "Network is down",
    "Network is unreachable",
    "Network dropped connection on reset",
    "Software caused connection abort",
    "Connection reset by peer",
    "No buffer space available",
    "Transport endpoint is already connected",
    "Transport endpoint is not connected",
    "Destination address required",
    "Cannot send after transport endpoint shutdown",
    "Too many references: cannot splice",
    "Connection timed out",
    "Connection refused",
    "Too many levels of symbolic links",
    "File name too long",
    "Host is down",
    "No route to host",
    "Directory not empty",
    "Too many processes",
    "Too many users",
    "Disk quota exceeded",
    "Stale NFS file handle",
    "Object is remote",
    "RPC struct is bad",
    "RPC version wrong",
    "RPC program not available",
    "RPC program version wrong",
    "RPC bad procedure for program",
    "No locks available",
    "Inappropriate file type or format",
    "Authentication error",
    "Need authenticator",
    "Function not implemented",
    "Not supported",
    "Invalid or incomplete multibyte or wide character",
    "Inappropriate operation for background process",
    "Translator died",
    "You really blew it this time",
    "Computer bought the farm",
    "Gratuitous error",
    "Bad message",
    "Identifier removed",
    "Multihop attempted",
    "No data available",
    "Link has been severed",
    "No message of desired type",
    "Out of streams resources",
    "Device not a stream",
    "Value too large for defined data type",
    "Protocol error",
    "Timer expired",
    "Operation canceled",
    "Interrupted system call should be restarted",
    "Channel number out of range",
    "Level 2 not synchronized",
    "Level 3 halted",
    "Level 3 reset",
    "Link number out of range",
    "Protocol driver not attached",
    "No CSI structure available",
    "Level 2 halted",
    "Invalid exchange",
    "Invalid request descriptor",
    "Exchange full",
    "No anode",
    "Invalid request code",
    "Invalid slot",
    "File locking deadlock error",
    "Bad font file format",
    "Machine is not on the network",
    "Package not installed",
    "Advertise error",
    "Srmount error",
    "Communication error on send",
    "RFS specific error",
    "Name not unique on network",
    "File descriptor in bad state",
    "Remote address changed",
    "Can not access a needed shared library",
    "Accessing a corrupted shared library",
    ".lib section in a.out corrupted",
    "Attempting to link in too many shared libraries",
    "Cannot exec a shared library directly",
    "Streams pipe error",
    "Structure needs cleaning",
    "Not a XENIX named type file",
    "No XENIX semaphores available",
    "Is a named type file",
    "Remote I/O error",
    "No medium found",
    "Wrong medium type",
    "Required key not available",
    "Key has expired",
    "Key has been revoked",
    "Key was rejected by service",
    "Owner died",
    "State not recoverable"
	      ]

# list of signals as defined in glibc from sysdeps/generic/siglist.h
signals = [
  "Hangup",
  "Interrupt",
  "Quit",
  "Illegal instruction",
  "Trace/breakpoint trap",
  "Aborted",
  "Floating point exception",
  "Killed",
  "Bus error",
  "Segmentation fault",
  "Broken pipe",
  "Alarm clock",
  "Terminated",
  "Urgent I/O condition",
  "Stopped (signal)",
  "Stopped",
  "Continued",
  "Child exited",
  "Stopped (tty input)",
  "Stopped (tty output)",
  "I/O possible",
  "CPU time limit exceeded",
  "File size limit exceeded",
  "Virtual timer expired",
  "Profiling timer expired",
  "Window changed",
  "User defined signal 1",
  "User defined signal 2",
  "EMT trap",
  "Bad system call",
  "Stack fault",
  "Information request",
  "Power failure",
  "Resource lost"
	  ]

## paths extracted from glibc:
## resolv/netdb.h
## sysdeps/unix/sysv/linux/paths.h

paths = [ "/bin/csh"
	, "/bin/sh"
	, "/boot/vmlinux"
	, "/dev/"
	, "/dev/console"
	, "/dev/drum"
	, "/dev/kmem"
	, "/dev/mem"
	, "/dev/null"
	, "/dev/tty"
	, "/etc/fstab"
	, "/etc/hosts.equiv"
	, "/etc/hosts"
	, "/etc/mtab"
	, "/etc/networks"
	, "/etc/nologin"
	, "/etc/nsswitch.conf"
	, "/etc/protocols"
	, "/etc/services"
	, "/etc/shadow"
	, "/etc/shells"
	, "/proc/kmsg"
	, "/tmp/"
	, "/usr/sbin/sendmail"
	, "/usr/share/man"
	, "/usr/bin/vi"
	, "/var/db/"
	, "/var/log/lastlog"
	, "/var/log/wtmp"
	, "/var/mail"
	, "/var/lib"
	, "/var/run/"
	, "/var/run/dev.db"
	, "/var/run/utmp"
	, "/var/spool/rwho"
	, "/var/tmp/"
        ]

## Sun RPC from sunrpc/pmap_rmt.c in glibc and libc/inet/rpc/pmap_rmt.c in uClibc

## times, dates, from locale/C-time.c in glibc, test/locale/tst-C-locale.c in uClibc

timedates = [ "Sun",
              "Mon",
              "Tue",
              "Wed",
              "Thu",
              "Fri",
              "Sat",
              "Sunday",
              "Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday",
              "Saturday",
              "Jan",
              "Feb",
              "Mar",
              "Apr",
              "May",
              "Jun",
              "Jul",
              "Aug",
              "Sep",
              "Oct",
              "Nov",
              "Dec",
              "January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December",
              "AM",
              "PM",
              "%a %b %e %H:%M:%S %Y",
              "%m/%d/%y",
              "%H:%M:%S",
              "%I:%M:%S %p"
              ]
