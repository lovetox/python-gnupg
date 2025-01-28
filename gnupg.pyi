"""
This type stub file was generated by pyright.
"""

from typing import Any

__version__: str = ...
__author__: str = ...
__date__: str = ...

from typing import Protocol

class ReadableFile(Protocol):
    def read(self, size: int) -> bytes: ...
    
class StatusHandler:
    """
    The base class for handling status messages from `gpg`.
    """

    on_data_failure = ...
    def __init__(self, gpg: GPG) -> None:
        """
        Initialize an instance.

        Args:
            gpg (GPG): The :class:`GPG` instance in use.
        """
        ...

    def handle_status(self, key: str, value: str) -> None:
        """
        Handle status messages from the `gpg` child process. These are lines of the format

            [GNUPG:] <key> <value>

        Args:
            key (str): Identifies what the status message is.
            value (str): Identifies additional data, which differs depending on the key.
        """
        ...

class Verify(StatusHandler):
    """
    This class handles status messages during signature verificaton.
    """

    TRUST_EXPIRED: int = ...
    TRUST_UNDEFINED: int = ...
    TRUST_NEVER: int = ...
    TRUST_MARGINAL: int = ...
    TRUST_FULLY: int = ...
    TRUST_ULTIMATE: int = ...
    TRUST_LEVELS: dict[str, int] = ...
    GPG_SYSTEM_ERROR_CODES: dict[int, str] = ...
    GPG_ERROR_CODES: dict[int, str] = ...
    returncode = ...
    def __init__(self, gpg: GPG) -> None: ...
    def __nonzero__(self) -> bool: ...

    __bool__ = ...
    def handle_status(self, key: str, value: str) -> None: ...

class ImportResult(StatusHandler):
    """
    This class handles status messages during key import.
    """

    counts = ...
    returncode = ...
    def __init__(self, gpg: GPG) -> None: ...
    def __nonzero__(self) -> bool: ...

    __bool__ = ...
    ok_reason: dict[str, str] = ...
    problem_reason: dict[str, str] = ...
    def handle_status(self, key: str, value: str) -> None: ...
    def summary(self) -> str:
        """
        Return a summary indicating how many keys were imported and how many were not imported.
        """
        ...

ESCAPE_PATTERN = ...
BASIC_ESCAPES = ...

class SendResult(StatusHandler):
    """
    This class handles status messages during key sending.
    """

    returncode = ...
    def handle_status(self, key: str, value: str) -> None: ...

class SearchKeys(StatusHandler, list[dict[Any, Any]]):
    """
    This class handles status messages during key search.
    """

    UID_INDEX = ...
    FIELDS = ...
    returncode = ...
    def __init__(self, gpg: GPG) -> None: ...
    def get_fields(self, args: Any) -> dict[str, Any]:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

    def pub(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

    def uid(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

    def handle_status(self, key: str, value: str) -> None: ...

class ListKeys(SearchKeys):
    """
    This class handles status messages during listing keys and signatures.

    Handle pub and uid (relating the latter to the former).

    We don't care about (info from GnuPG DETAILS file):

    crt = X.509 certificate
    crs = X.509 certificate and private key available
    uat = user attribute (same as user id except for field 10).
    sig = signature
    rev = revocation signature
    pkd = public key data (special field format, see below)
    grp = reserved for gpgsm
    rvk = revocation key
    """

    UID_INDEX = ...
    FIELDS = ...
    def __init__(self, gpg: GPG) -> None: ...
    def key(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...
    sec = ...
    def fpr(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

    def grp(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

    def sub(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

    def ssb(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

    def sig(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

class ScanKeys(ListKeys):
    """
    This class handles status messages during scanning keys.
    """

    def sub(self, args: Any) -> None:
        """
        Internal method used to update the instance from a `gpg` status message.
        """
        ...

class TextHandler: ...

_INVALID_KEY_REASONS = ...

class Crypt(Verify, TextHandler):
    """
    This class handles status messages during encryption and decryption.
    """

    def __init__(self, gpg: GPG) -> None: ...
    def __nonzero__(self) -> bool: ...

    __bool__ = ...
    def handle_status(self, key: str, value: str) -> None: ...

class GenKey(StatusHandler):
    """
    This class handles status messages during key generation.
    """

    returncode = ...
    def __init__(self, gpg: GPG) -> None: ...
    def __nonzero__(self) -> bool: ...

    __bool__ = ...
    def __str__(self) -> str: ...
    def handle_status(self, key: str, value: str) -> None: ...

class AddSubkey(StatusHandler):
    """
    This class handles status messages during subkey addition.
    """

    returncode = ...
    def __init__(self, gpg: GPG) -> None: ...
    def __nonzero__(self) -> bool: ...

    __bool__ = ...
    def __str__(self) -> str: ...
    def handle_status(self, key: str, value: str) -> None: ...

class ExportResult(GenKey):
    """
    This class handles status messages during key export.
    """

    def handle_status(self, key: str, value: str) -> None: ...

class DeleteResult(StatusHandler):
    """
    This class handles status messages during key deletion.
    """

    returncode = ...
    def __init__(self, gpg: GPG) -> None: ...
    def __str__(self) -> str: ...

    problem_reason = ...
    def handle_status(self, key: str, value: str) -> None: ...
    def __nonzero__(self) -> bool: ...

    __bool__ = ...

class TrustResult(DeleteResult):
    """
    This class handles status messages during key trust setting.
    """

    ...

class Sign(StatusHandler, TextHandler):
    """
    This class handles status messages during signing.
    """

    returncode = ...
    def __init__(self, gpg: GPG) -> None: ...
    def __nonzero__(self) -> bool: ...

    __bool__ = ...
    def handle_status(self, key: str, value: str) -> None: ...

class AutoLocateKey(StatusHandler):
    """
    This class handles status messages during key auto-locating.
    fingerprint: str
    key_length: int
    created_at: date
    email: str
    email_real_name: str
    """

    def __init__(self, gpg: GPG) -> None: ...
    def handle_status(self, key: str, value: str) -> None: ...
    def pub(self, args: Any) -> None:
        """
        Internal method to handle the 'pub' status message.
        `pub` message contains the fingerprint of the public key, its type and its creation date.
        """
        ...

    def uid(self, args: Any) -> None: ...
    def sub(self, args: Any) -> None: ...
    def fpr(self, args: Any) -> None: ...

VERSION_RE = ...
HEX_DIGITS_RE = ...
PUBLIC_KEY_RE = ...

class GPG:
    """
    This class provides a high-level programmatic interface for `gpg`.
    """

    error_map = ...
    decode_errors = ...
    buffer_size = ...
    result_map = ...
    def __init__(
        self,
        gpgbinary: str = ...,
        gnupghome: str | None = ...,
        verbose: bool = ...,
        use_agent: bool = ...,
        keyring: str | list[str] | None = ...,
        options: list[str] | None = ...,
        secret_keyring: str | list[str] | None = ...,
        env: dict[str, str] | None = ...,
    ) -> None:
        """Initialize a GPG process wrapper.

        Args:
            gpgbinary (str): A pathname for the GPG binary to use.

            gnupghome (str): A pathname to where we can find the public and private keyrings. The default is
                             whatever `gpg` defaults to.

            keyring (str|list): The name of alternative keyring file to use, or a list of such keyring files. If
                                specified, the default keyring is not used.

            options (list): A list of additional options to pass to the GPG binary.

            secret_keyring (str|list): The name of an alternative secret keyring file to use, or a list of such
                                       keyring files.

            env (dict): A dict of environment variables to be used for the GPG subprocess.
        """
        ...

    def make_args(self, args: list[str], passphrase: str) -> list[str]:
        """
        Make a list of command line elements for GPG. The value of ``args``
        will be appended. The ``passphrase`` argument needs to be True if
        a passphrase will be sent to `gpg`, else False.

        Args:
            args (list[str]): A list of arguments.
            passphrase (str): The passphrase to use.
        """
        ...

    def is_valid_file(self, fileobj: Any) -> bool:
        """
        A simplistic check for a file-like object.

        Args:
            fileobj (object): The object to test.
        Returns:
            bool: ``True`` if it's a file-like object, else ``False``.
        """
        ...

    def sign(self, message: str | bytes, **kwargs: Any) -> Sign:
        """
        Sign a message. This method delegates most of the work to the `sign_file()` method.

        Args:
            message (str|bytes): The data to sign.
            kwargs (dict): Keyword arguments, which are passed to `sign_file()`:

                * keyid (str): The key id of the signer.

                * passphrase (str): The passphrase for the key.

                * clearsign (bool): Whether to use clear signing.

                * detach (bool): Whether to produce a detached signature.

                * binary (bool): Whether to produce a binary signature.

                * output (str): The path to write a detached signature to.

                * extra_args (list[str]): Additional arguments to pass to `gpg`.
        """
        ...

    def set_output_without_confirmation(self, args: list[str], output: str) -> None:
        """
        If writing to a file which exists, avoid a confirmation message by
        updating the *args* value in place to set the output path and avoid
        any cpmfirmation prompt.

        Args:
            args (list[str]): A list of arguments.
            output (str): The path to the outpur file.
        """
        ...

    def is_valid_passphrase(self, passphrase: str) -> bool:
        """
        Confirm that the passphrase doesn't contain newline-type characters - it is passed in a pipe to `gpg`,
        and so not checking could lead to spoofing attacks by passing arbitrary text after passphrase and newline.

        Args:
            passphrase (str): The passphrase to test.

        Returns:
            bool: ``True`` if it's a valid passphrase, else ``False``.
        """
        ...

    def sign_file(
        self,
        fileobj_or_path: str | ReadableFile,
        keyid: str | None = ...,
        passphrase: str | None = ...,
        clearsign: bool = ...,
        detach: bool = ...,
        binary: bool = ...,
        output: str | None = ...,
        extra_args: list[str] | None = ...,
    ) -> Sign:
        """
        Sign data in a file or file-like object.

        Args:
            fileobj_or_path (str|file): The file or file-like object to sign.

            keyid (str): The key id of the signer.

            passphrase (str): The passphrase for the key.

            clearsign (bool): Whether to use clear signing.

            detach (bool): Whether to produce a detached signature.

            binary (bool): Whether to produce a binary signature.

            output (str): The path to write a detached signature to.

            extra_args (list[str]): Additional arguments to pass to `gpg`.
        """
        ...

    def verify(self, data: str | bytes, **kwargs: Any) -> Verify:
        """
        Verify the signature on the contents of the string *data*. This method delegates most of the work to
        `verify_file()`.

        Args:
            data (str|bytes): The data to verify.
            kwargs (dict): Keyword arguments, which are passed to `verify_file()`:

                * fileobj_or_path (str|file): A path to a signature, or a file-like object containing one.

                * data_filename (str): If the signature is a detached one, the path to the data that was signed.

                * close_file (bool): If a file-like object is passed in, whether to close it.

                * extra_args (list[str]): Additional arguments to pass to `gpg`.
        """
        ...

    def verify_file(
        self,
        fileobj_or_path: str | ReadableFile,
        data_filename: str | None = ...,
        close_file: bool = ...,
        extra_args: list[str] | None = ...,
    ) -> Verify:
        """
        Verify a signature.

        Args:
            fileobj_or_path (str|file): A path to a signature, or a file-like object containing one.

            data_filename (str): If the signature is a detached one, the path to the data that was signed.

            close_file (bool): If a file-like object is passed in, whether to close it.

            extra_args (list[str]): Additional arguments to pass to `gpg`.
        """
        ...

    def verify_data(
        self, sig_filename: str, data: str | bytes, extra_args: list[str] | None = ...
    ) -> Verify:
        """
        Verify the signature in sig_filename against data in memory

        Args:
            sig_filename (str): The path to a signature.

            data (str|bytes): The data to be verified.

            extra_args (list[str]): Additional arguments to pass to `gpg`.
        """
        ...

    def import_keys(
        self,
        key_data: str | bytes,
        extra_args: list[str] | None = ...,
        passphrase: str | None = ...,
    ) -> ImportResult:
        """
        Import the key_data into our keyring.

        Args:
            key_data (str|bytes): The key data to import.

            passphrase (str): The passphrase to use.

            extra_args (list[str]): Additional arguments to pass to `gpg`.
        """
        ...

    def import_keys_file(self, key_path: str, **kwargs: Any) -> ImportResult:
        """
        Import the key data in key_path into our keyring.

        Args:
            key_path (str): A path to the key data to be imported.
        """
        ...

    def recv_keys(self, keyserver: str, *keyids: str, **kwargs: Any) -> ImportResult:
        """
        Import one or more keys from a keyserver.

        Args:
            keyserver (str): The key server hostname.

            keyids (str): A list of key ids to receive.
        """
        ...

    def send_keys(self, keyserver: str, *keyids: str, **kwargs: Any) -> SendResult:
        """
        Send one or more keys to a keyserver.

        Args:
            keyserver (str): The key server hostname.

            keyids (list[str]): A list of key ids to send.
        """
        ...

    def delete_keys(
        self,
        fingerprints: str | list[str],
        secret: bool = ...,
        passphrase: str | None = ...,
        expect_passphrase: bool = ...,
        exclamation_mode: bool = ...,
    ) -> DeleteResult:
        """
        Delete the indicated keys.

        Args:
            fingerprints (str|list[str]): The keys to delete.

            secret (bool): Whether to delete secret keys.

            passphrase (str): The passphrase to use.

            expect_passphrase (bool): Whether a passphrase is expected.

            exclamation_mode (bool): If specified, a `'!'` is appended to each fingerprint. This deletes only a subkey
                                     or an entire key, depending on what the fingerprint refers to.

        .. note:: Passphrases

           Since GnuPG 2.1, you can't delete secret keys without providing a passphrase. However, if you're expecting
           the passphrase to go to `gpg` via pinentry, you should specify expect_passphrase=False. (It's only checked
           for GnuPG >= 2.1).
        """
        ...

    def export_keys(
        self,
        keyids: str | list[str],
        secret: bool = ...,
        armor: bool = ...,
        minimal: bool = ...,
        passphrase: str | None = ...,
        expect_passphrase: bool = ...,
        output: str | None = ...,
    ) -> ExportResult:
        """
        Export the indicated keys. A 'keyid' is anything `gpg` accepts.

        Args:
            keyids (str|list[str]): A single keyid or a list of them.

            secret (bool): Whether to export secret keys.

            armor (bool): Whether to ASCII-armor the output.

            minimal (bool): Whether to pass `--export-options export-minimal` to `gpg`.

            passphrase (str): The passphrase to use.

            expect_passphrase (bool): Whether a passphrase is expected.

            output (str): If specified, the path to write the exported key(s) to.

        .. note:: Passphrases

           Since GnuPG 2.1, you can't export secret keys without providing a passphrase. However, if you're expecting
           the passphrase to go to `gpg` via pinentry, you should specify expect_passphrase=False. (It's only checked
           for GnuPG >= 2.1).
        """
        ...

    def list_keys(
        self, secret: bool = ..., keys: str | list[str] | None = ..., sigs: bool = ...
    ) -> ListKeys:
        """
        List the keys currently in the keyring.

        Args:
            secret (bool): Whether to list secret keys.

            keys (str|list[str]): A list of key ids to match.

            sigs (bool): Whether to include signature information.

        Returns:
            list[dict]: A list of dictionaries with key information.
        """
        ...

    def scan_keys(self, filename: str) -> ScanKeys:
        """
        List details of an ascii armored or binary key file without first importing it to the local keyring.

        Args:
            filename (str): The path to the file containing the key(s).

        .. warning:: Warning:
            Care is needed. The function works on modern GnuPG by running:

                $ gpg --dry-run --import-options import-show --import filename

            On older versions, it does the *much* riskier:

                $ gpg --with-fingerprint --with-colons filename
        """
        ...

    def scan_keys_mem(self, key_data: str | bytes) -> ScanKeys:
        """
        List details of an ascii armored or binary key without first importing it to the local keyring.

        Args:
            key_data (str|bytes): The key data to import.

        .. warning:: Warning:
            Care is needed. The function works on modern GnuPG by running:

                $ gpg --dry-run --import-options import-show --import filename

            On older versions, it does the *much* riskier:

                $ gpg --with-fingerprint --with-colons filename
        """
        ...

    def search_keys(
        self, query: str, keyserver: str = ..., extra_args: list[str] | None = ...
    ) -> SearchKeys:
        """
        search a keyserver by query (using the `--search-keys` option).

        Args:
            query(str): The query to use.

            keyserver (str): The key server hostname.

            extra_args (list[str]): Additional arguments to pass to `gpg`.
        """
        ...

    def auto_locate_key(
        self, email: str, mechanisms: list[str] | None = ..., **kwargs: Any
    ) -> AutoLocateKey:
        """
        Auto locate a public key by `email`.

        Args:
            email (str): The email address to search for.
            mechanisms (list[str]): A list of mechanisms to use. Valid mechanisms can be found
            here https://www.gnupg.org/documentation/manuals/gnupg/GPG-Configuration-Options.html
            under "--auto-key-locate". Default: ['wkd', 'ntds', 'ldap', 'cert', 'dane', 'local']
        """
        ...

    def gen_key(self, input: str) -> GenKey:
        """
        Generate a key; you might use `gen_key_input()` to create the input.

        Args:
            input (str): The input to the key creation operation.
        """
        ...

    def gen_key_input(self, **kwargs: Any) -> str:
        """
        Generate `--gen-key` input  (see `gpg` documentation in DETAILS).

        Args:
            kwargs (dict): A list of keyword arguments.
        Returns:
            str: A string suitable for passing to the `gen_key()` method.
        """
        ...

    def add_subkey(
        self,
        master_key: str,
        master_passphrase: str | None = ...,
        algorithm: str = ...,
        usage: str = ...,
        expire: str = ...,
    ) -> AddSubkey:
        """
        Add subkeys to a master key,

        Args:
            master_key (str): The master key.

            master_passphrase (str): The passphrase for the master key.

            algorithm (str): The key algorithm to use.

            usage (str): The desired uses for the subkey.

            expire (str): The expiration date of the subkey.
        """
        ...

    def encrypt_file(
        self,
        fileobj_or_path: str | ReadableFile,
        recipients: str | list[str],
        sign: str | None = ...,
        always_trust: bool = ...,
        passphrase: str | None = ...,
        armor: bool = ...,
        output: str | None = ...,
        symmetric: bool = ...,
        extra_args: list[str] | None = ...,
    ) -> Crypt:
        """
        Encrypt data in a file or file-like object.

        Args:
            fileobj_or_path (str|file): A path to a file or a file-like object containing the data to be encrypted.

            recipients (str|list): A key id of a recipient of the encrypted data, or a list of such key ids.

            sign (str): If specified, the key id of a signer to sign the encrypted data.

            always_trust (bool): Whether to always trust keys.

            passphrase (str): The passphrase to use for a signature.

            armor (bool): Whether to ASCII-armor the output.

            output (str): A path to write the encrypted output to.

            symmetric (bool): Whether to use symmetric encryption,

            extra_args (list[str]): A list of additional arguments to pass to `gpg`.
        """
        ...

    def encrypt(
        self, data: str | bytes, recipients: str | list[str], **kwargs: Any
    ) -> Crypt:
        """
        Encrypt the message contained in the string *data* for *recipients*. This method delegates most of the work to
        `encrypt_file()`.

        Args:
            data (str|bytes): The data to encrypt.

            recipients (str|list[str]): A key id of a recipient of the encrypted data, or a list of such key ids.

            kwargs (dict): Keyword arguments, which are passed to `encrypt_file()`:
                * sign (str): If specified, the key id of a signer to sign the encrypted data.

                * always_trust (bool): Whether to always trust keys.

                * passphrase (str): The passphrase to use for a signature.

                * armor (bool): Whether to ASCII-armor the output.

                * output (str): A path to write the encrypted output to.

                * symmetric (bool): Whether to use symmetric encryption,

                * extra_args (list[str]): A list of additional arguments to pass to `gpg`.
        """
        ...

    def decrypt(self, message: str | bytes, **kwargs: Any) -> Crypt:
        """
        Decrypt the data in *message*. This method delegates most of the work to
        `decrypt_file()`.

        Args:
            message (str|bytes): The data to decrypt. A default key will be used for decryption.

            kwargs (dict): Keyword arguments, which are passed to `decrypt_file()`:

                * always_trust: Whether to always trust keys.

                * passphrase (str): The passphrase to use.

                * output (str): If specified, the path to write the decrypted data to.

                * extra_args (list[str]): A list of extra arguments to pass to `gpg`.
        """
        ...

    def decrypt_file(
        self,
        fileobj_or_path: str | ReadableFile,
        always_trust: bool = ...,
        passphrase: str | None = ...,
        output: str | None = ...,
        extra_args: list[str] | None = ...,
    ) -> Crypt:
        """
        Decrypt data in a file or file-like object.

        Args:
            fileobj_or_path (str|file): A path to a file or a file-like object containing the data to be decrypted.

            always_trust: Whether to always trust keys.

            passphrase (str): The passphrase to use.

            output (str): If specified, the path to write the decrypted data to.

            extra_args (list[str]): A list of extra arguments to pass to `gpg`.
        """
        ...

    def get_recipients(self, message: str | bytes, **kwargs: Any) -> list[str]:
        """Get the list of recipients for an encrypted message. This method delegates most of the work to
        `get_recipients_file()`.

        Args:
            message (str|bytes): The encrypted message.

            kwargs (dict): Keyword arguments, which are passed to `get_recipients_file()`:

                * extra_args (list[str]): A list of extra arguments to pass to `gpg`.
        """
        ...

    def get_recipients_file(
        self, fileobj_or_path: Any, extra_args: list[str] | None = ...
    ) -> list[str]:
        """
        Get the list of recipients for an encrypted message in a file or file-like object.

        Args:
            fileobj_or_path (str|file): A path to a file or file-like object containing the encrypted data.

            extra_args (list[str]): A list of extra arguments to pass to `gpg`.
        """
        ...

    def trust_keys(self, fingerprints: str | list[str], trustlevel: str) -> TrustResult:
        """
        Set the trust level for one or more keys.

        Args:
            fingerprints (str|list[str]): A key id for which to set the trust level, or a list of such key ids.

            trustlevel (str): The trust level. This is one of the following.

                                  * ``'TRUST_EXPIRED'``
                                  * ``'TRUST_UNDEFINED'``
                                  * ``'TRUST_NEVER'``
                                  * ``'TRUST_MARGINAL'``
                                  * ``'TRUST_FULLY'``
                                  * ``'TRUST_ULTIMATE'``
        """
        ...
