# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trpc.proto\x12\tprotowire\"\x1b\n\x08RPCError\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x9b\x01\n\x08RpcBlock\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.protowire.RpcBlockHeader\x12/\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x19.protowire.RpcTransaction\x12\x33\n\x0bverboseData\x18\x03 \x01(\x0b\x32\x1e.protowire.RpcBlockVerboseData\"\x9e\x02\n\x0eRpcBlockHeader\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x30\n\x07parents\x18\x0c \x03(\x0b\x32\x1f.protowire.RpcBlockLevelParents\x12\x16\n\x0ehashMerkleRoot\x18\x03 \x01(\t\x12\x1c\n\x14\x61\x63\x63\x65ptedIdMerkleRoot\x18\x04 \x01(\t\x12\x16\n\x0eutxoCommitment\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x12\x0c\n\x04\x62its\x18\x07 \x01(\r\x12\r\n\x05nonce\x18\x08 \x01(\x04\x12\x10\n\x08\x64\x61\x61Score\x18\t \x01(\x04\x12\x10\n\x08\x62lueWork\x18\n \x01(\t\x12\x14\n\x0cpruningPoint\x18\x0e \x01(\t\x12\x11\n\tblueScore\x18\r \x01(\x04\",\n\x14RpcBlockLevelParents\x12\x14\n\x0cparentHashes\x18\x01 \x03(\t\"\xfb\x01\n\x13RpcBlockVerboseData\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x12\n\ndifficulty\x18\x0b \x01(\x01\x12\x1a\n\x12selectedParentHash\x18\r \x01(\t\x12\x16\n\x0etransactionIds\x18\x0e \x03(\t\x12\x14\n\x0cisHeaderOnly\x18\x0f \x01(\x08\x12\x11\n\tblueScore\x18\x10 \x01(\x04\x12\x16\n\x0e\x63hildrenHashes\x18\x11 \x03(\t\x12\x1b\n\x13mergeSetBluesHashes\x18\x12 \x03(\t\x12\x1a\n\x12mergeSetRedsHashes\x18\x13 \x03(\t\x12\x14\n\x0cisChainBlock\x18\x14 \x01(\x08\"\x84\x02\n\x0eRpcTransaction\x12\x0f\n\x07version\x18\x01 \x01(\r\x12.\n\x06inputs\x18\x02 \x03(\x0b\x32\x1e.protowire.RpcTransactionInput\x12\x30\n\x07outputs\x18\x03 \x03(\x0b\x32\x1f.protowire.RpcTransactionOutput\x12\x10\n\x08lockTime\x18\x04 \x01(\x04\x12\x14\n\x0csubnetworkId\x18\x05 \x01(\t\x12\x0b\n\x03gas\x18\x06 \x01(\x04\x12\x0f\n\x07payload\x18\x08 \x01(\t\x12\x39\n\x0bverboseData\x18\t \x01(\x0b\x32$.protowire.RpcTransactionVerboseData\"\xc6\x01\n\x13RpcTransactionInput\x12\x30\n\x10previousOutpoint\x18\x01 \x01(\x0b\x32\x16.protowire.RpcOutpoint\x12\x17\n\x0fsignatureScript\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x12\n\nsigOpCount\x18\x05 \x01(\r\x12>\n\x0bverboseData\x18\x04 \x01(\x0b\x32).protowire.RpcTransactionInputVerboseData\">\n\x12RpcScriptPublicKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x17\n\x0fscriptPublicKey\x18\x02 \x01(\t\"\x9f\x01\n\x14RpcTransactionOutput\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x36\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1d.protowire.RpcScriptPublicKey\x12?\n\x0bverboseData\x18\x03 \x01(\x0b\x32*.protowire.RpcTransactionOutputVerboseData\"3\n\x0bRpcOutpoint\x12\x15\n\rtransactionId\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\"\x81\x01\n\x0cRpcUtxoEntry\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x36\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1d.protowire.RpcScriptPublicKey\x12\x15\n\rblockDaaScore\x18\x03 \x01(\x04\x12\x12\n\nisCoinbase\x18\x04 \x01(\x08\"t\n\x19RpcTransactionVerboseData\x12\x15\n\rtransactionId\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x0c\n\x04mass\x18\x04 \x01(\x04\x12\x11\n\tblockHash\x18\x0c \x01(\t\x12\x11\n\tblockTime\x18\x0e \x01(\x04\" \n\x1eRpcTransactionInputVerboseData\"^\n\x1fRpcTransactionOutputVerboseData\x12\x1b\n\x13scriptPublicKeyType\x18\x05 \x01(\t\x12\x1e\n\x16scriptPublicKeyAddress\x18\x06 \x01(\t\"!\n\x1fGetCurrentNetworkRequestMessage\"_\n GetCurrentNetworkResponseMessage\x12\x16\n\x0e\x63urrentNetwork\x18\x01 \x01(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"Z\n\x19SubmitBlockRequestMessage\x12\"\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x13.protowire.RpcBlock\x12\x19\n\x11\x61llowNonDAABlocks\x18\x03 \x01(\x08\"\xc7\x01\n\x1aSubmitBlockResponseMessage\x12H\n\x0crejectReason\x18\x01 \x01(\x0e\x32\x32.protowire.SubmitBlockResponseMessage.RejectReason\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\":\n\x0cRejectReason\x12\x08\n\x04NONE\x10\x00\x12\x11\n\rBLOCK_INVALID\x10\x01\x12\r\n\tIS_IN_IBD\x10\x02\"G\n\x1eGetBlockTemplateRequestMessage\x12\x12\n\npayAddress\x18\x01 \x01(\t\x12\x11\n\textraData\x18\x02 \x01(\t\"|\n\x1fGetBlockTemplateResponseMessage\x12\"\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x13.protowire.RpcBlock\x12\x10\n\x08isSynced\x18\x02 \x01(\x08\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\" \n\x1eNotifyBlockAddedRequestMessage\"F\n\x1fNotifyBlockAddedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"C\n\x1d\x42lockAddedNotificationMessage\x12\"\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x13.protowire.RpcBlock\" \n\x1eGetPeerAddressesRequestMessage\"\xd2\x01\n\x1fGetPeerAddressesResponseMessage\x12\x41\n\taddresses\x18\x01 \x03(\x0b\x32..protowire.GetPeerAddressesKnownAddressMessage\x12G\n\x0f\x62\x61nnedAddresses\x18\x02 \x03(\x0b\x32..protowire.GetPeerAddressesKnownAddressMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"3\n#GetPeerAddressesKnownAddressMessage\x12\x0c\n\x04\x41\x64\x64r\x18\x01 \x01(\t\"\"\n GetSelectedTipHashRequestMessage\"a\n!GetSelectedTipHashResponseMessage\x12\x17\n\x0fselectedTipHash\x18\x01 \x01(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"g\n\x1dGetMempoolEntryRequestMessage\x12\x0c\n\x04txId\x18\x01 \x01(\t\x12\x19\n\x11includeOrphanPool\x18\x02 \x01(\x08\x12\x1d\n\x15\x66ilterTransactionPool\x18\x03 \x01(\x08\"m\n\x1eGetMempoolEntryResponseMessage\x12&\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x17.protowire.MempoolEntry\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"[\n\x1fGetMempoolEntriesRequestMessage\x12\x19\n\x11includeOrphanPool\x18\x01 \x01(\x08\x12\x1d\n\x15\x66ilterTransactionPool\x18\x02 \x01(\x08\"q\n GetMempoolEntriesResponseMessage\x12(\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x17.protowire.MempoolEntry\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"]\n\x0cMempoolEntry\x12\x0b\n\x03\x66\x65\x65\x18\x01 \x01(\x04\x12.\n\x0btransaction\x18\x03 \x01(\x0b\x32\x19.protowire.RpcTransaction\x12\x10\n\x08isOrphan\x18\x04 \x01(\x08\"$\n\"GetConnectedPeerInfoRequestMessage\"\x81\x01\n#GetConnectedPeerInfoResponseMessage\x12\x35\n\x05infos\x18\x01 \x03(\x0b\x32&.protowire.GetConnectedPeerInfoMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\xdc\x01\n\x1bGetConnectedPeerInfoMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x18\n\x10lastPingDuration\x18\x03 \x01(\x03\x12\x12\n\nisOutbound\x18\x06 \x01(\x08\x12\x12\n\ntimeOffset\x18\x07 \x01(\x03\x12\x11\n\tuserAgent\x18\x08 \x01(\t\x12!\n\x19\x61\x64vertisedProtocolVersion\x18\t \x01(\r\x12\x15\n\rtimeConnected\x18\n \x01(\x03\x12\x11\n\tisIbdPeer\x18\x0b \x01(\x08\"=\n\x15\x41\x64\x64PeerRequestMessage\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x13\n\x0bisPermanent\x18\x02 \x01(\x08\"=\n\x16\x41\x64\x64PeerResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"f\n\x1fSubmitTransactionRequestMessage\x12.\n\x0btransaction\x18\x01 \x01(\x0b\x32\x19.protowire.RpcTransaction\x12\x13\n\x0b\x61llowOrphan\x18\x02 \x01(\x08\"^\n SubmitTransactionResponseMessage\x12\x15\n\rtransactionId\x18\x01 \x01(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"^\n5NotifyVirtualSelectedParentChainChangedRequestMessage\x12%\n\x1dincludeAcceptedTransactionIds\x18\x01 \x01(\x08\"]\n6NotifyVirtualSelectedParentChainChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\xb9\x01\n4VirtualSelectedParentChainChangedNotificationMessage\x12\x1f\n\x17removedChainBlockHashes\x18\x01 \x03(\t\x12\x1d\n\x15\x61\x64\x64\x65\x64\x43hainBlockHashes\x18\x03 \x03(\t\x12\x41\n\x16\x61\x63\x63\x65ptedTransactionIds\x18\x02 \x03(\x0b\x32!.protowire.AcceptedTransactionIds\"C\n\x16GetBlockRequestMessage\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x1b\n\x13includeTransactions\x18\x03 \x01(\x08\"b\n\x17GetBlockResponseMessage\x12\"\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x13.protowire.RpcBlock\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"3\n\x1bGetSubnetworkRequestMessage\x12\x14\n\x0csubnetworkId\x18\x01 \x01(\t\"U\n\x1cGetSubnetworkResponseMessage\x12\x10\n\x08gasLimit\x18\x01 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"p\n4GetVirtualSelectedParentChainFromBlockRequestMessage\x12\x11\n\tstartHash\x18\x01 \x01(\t\x12%\n\x1dincludeAcceptedTransactionIds\x18\x02 \x01(\x08\"T\n\x16\x41\x63\x63\x65ptedTransactionIds\x12\x1a\n\x12\x61\x63\x63\x65ptingBlockHash\x18\x01 \x01(\t\x12\x1e\n\x16\x61\x63\x63\x65ptedTransactionIds\x18\x02 \x03(\t\"\xdf\x01\n5GetVirtualSelectedParentChainFromBlockResponseMessage\x12\x1f\n\x17removedChainBlockHashes\x18\x01 \x03(\t\x12\x1d\n\x15\x61\x64\x64\x65\x64\x43hainBlockHashes\x18\x03 \x03(\t\x12\x41\n\x16\x61\x63\x63\x65ptedTransactionIds\x18\x02 \x03(\x0b\x32!.protowire.AcceptedTransactionIds\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"^\n\x17GetBlocksRequestMessage\x12\x0f\n\x07lowHash\x18\x01 \x01(\t\x12\x15\n\rincludeBlocks\x18\x02 \x01(\x08\x12\x1b\n\x13includeTransactions\x18\x03 \x01(\x08\"y\n\x18GetBlocksResponseMessage\x12\x13\n\x0b\x62lockHashes\x18\x04 \x03(\t\x12#\n\x06\x62locks\x18\x03 \x03(\x0b\x32\x13.protowire.RpcBlock\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1d\n\x1bGetBlockCountRequestMessage\"l\n\x1cGetBlockCountResponseMessage\x12\x12\n\nblockCount\x18\x01 \x01(\x04\x12\x13\n\x0bheaderCount\x18\x02 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1f\n\x1dGetBlockDagInfoRequestMessage\"\x92\x02\n\x1eGetBlockDagInfoResponseMessage\x12\x13\n\x0bnetworkName\x18\x01 \x01(\t\x12\x12\n\nblockCount\x18\x02 \x01(\x04\x12\x13\n\x0bheaderCount\x18\x03 \x01(\x04\x12\x11\n\ttipHashes\x18\x04 \x03(\t\x12\x12\n\ndifficulty\x18\x05 \x01(\x01\x12\x16\n\x0epastMedianTime\x18\x06 \x01(\x03\x12\x1b\n\x13virtualParentHashes\x18\x07 \x03(\t\x12\x18\n\x10pruningPointHash\x18\x08 \x01(\t\x12\x17\n\x0fvirtualDaaScore\x18\t \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"B\n%ResolveFinalityConflictRequestMessage\x12\x19\n\x11\x66inalityBlockHash\x18\x01 \x01(\t\"M\n&ResolveFinalityConflictResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\'\n%NotifyFinalityConflictsRequestMessage\"M\n&NotifyFinalityConflictsResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"A\n#FinalityConflictNotificationMessage\x12\x1a\n\x12violatingBlockHash\x18\x01 \x01(\t\"H\n+FinalityConflictResolvedNotificationMessage\x12\x19\n\x11\x66inalityBlockHash\x18\x01 \x01(\t\"\x18\n\x16ShutDownRequestMessage\">\n\x17ShutDownResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"Q\n\x18GetHeadersRequestMessage\x12\x11\n\tstartHash\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x04\x12\x13\n\x0bisAscending\x18\x03 \x01(\x08\"Q\n\x19GetHeadersResponseMessage\x12\x0f\n\x07headers\x18\x01 \x03(\t\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"5\n NotifyUtxosChangedRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\"H\n!NotifyUtxosChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x85\x01\n\x1fUtxosChangedNotificationMessage\x12/\n\x05\x61\x64\x64\x65\x64\x18\x01 \x03(\x0b\x32 .protowire.UtxosByAddressesEntry\x12\x31\n\x07removed\x18\x02 \x03(\x0b\x32 .protowire.UtxosByAddressesEntry\"~\n\x15UtxosByAddressesEntry\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12(\n\x08outpoint\x18\x02 \x01(\x0b\x32\x16.protowire.RpcOutpoint\x12*\n\tutxoEntry\x18\x03 \x01(\x0b\x32\x17.protowire.RpcUtxoEntry\"<\n\'StopNotifyingUtxosChangedRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\"O\n(StopNotifyingUtxosChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"6\n!GetUtxosByAddressesRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\"|\n\"GetUtxosByAddressesResponseMessage\x12\x31\n\x07\x65ntries\x18\x01 \x03(\x0b\x32 .protowire.UtxosByAddressesEntry\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"4\n!GetBalanceByAddressRequestMessage\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"Z\n\"GetBalanceByAddressResponseMessage\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"9\n$GetBalancesByAddressesRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\"_\n\x16\x42\x61lancesByAddressEntry\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x80\x01\n%GetBalancesByAddressesResponseMessage\x12\x32\n\x07\x65ntries\x18\x01 \x03(\x0b\x32!.protowire.BalancesByAddressEntry\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"1\n/GetVirtualSelectedParentBlueScoreRequestMessage\"j\n0GetVirtualSelectedParentBlueScoreResponseMessage\x12\x11\n\tblueScore\x18\x01 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\";\n9NotifyVirtualSelectedParentBlueScoreChangedRequestMessage\"a\n:NotifyVirtualSelectedParentBlueScoreChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"b\n8VirtualSelectedParentBlueScoreChangedNotificationMessage\x12&\n\x1evirtualSelectedParentBlueScore\x18\x01 \x01(\x04\",\n*NotifyVirtualDaaScoreChangedRequestMessage\"R\n+NotifyVirtualDaaScoreChangedResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"D\n)VirtualDaaScoreChangedNotificationMessage\x12\x17\n\x0fvirtualDaaScore\x18\x01 \x01(\x04\"1\n/NotifyPruningPointUTXOSetOverrideRequestMessage\"W\n0NotifyPruningPointUTXOSetOverrideResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"0\n.PruningPointUTXOSetOverrideNotificationMessage\"8\n6StopNotifyingPruningPointUTXOSetOverrideRequestMessage\"^\n7StopNotifyingPruningPointUTXOSetOverrideResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1f\n\x11\x42\x61nRequestMessage\x12\n\n\x02ip\x18\x01 \x01(\t\"9\n\x12\x42\x61nResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"!\n\x13UnbanRequestMessage\x12\n\n\x02ip\x18\x01 \x01(\t\";\n\x14UnbanResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x17\n\x15GetInfoRequestMessage\"\xa1\x01\n\x16GetInfoResponseMessage\x12\r\n\x05p2pId\x18\x01 \x01(\t\x12\x13\n\x0bmempoolSize\x18\x02 \x01(\x04\x12\x15\n\rserverVersion\x18\x03 \x01(\t\x12\x15\n\risUtxoIndexed\x18\x04 \x01(\x08\x12\x10\n\x08isSynced\x18\x05 \x01(\x08\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"U\n,EstimateNetworkHashesPerSecondRequestMessage\x12\x12\n\nwindowSize\x18\x01 \x01(\r\x12\x11\n\tstartHash\x18\x02 \x01(\t\"t\n-EstimateNetworkHashesPerSecondResponseMessage\x12\x1e\n\x16networkHashesPerSecond\x18\x01 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"&\n$NotifyNewBlockTemplateRequestMessage\"L\n%NotifyNewBlockTemplateResponseMessage\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"%\n#NewBlockTemplateNotificationMessage\"~\n\x15MempoolEntryByAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12(\n\x07sending\x18\x02 \x03(\x0b\x32\x17.protowire.MempoolEntry\x12*\n\treceiving\x18\x03 \x03(\x0b\x32\x17.protowire.MempoolEntry\"y\n*GetMempoolEntriesByAddressesRequestMessage\x12\x11\n\taddresses\x18\x01 \x03(\t\x12\x19\n\x11includeOrphanPool\x18\x02 \x01(\x08\x12\x1d\n\x15\x66ilterTransactionPool\x18\x03 \x01(\x08\"\x85\x01\n+GetMempoolEntriesByAddressesResponseMessage\x12\x31\n\x07\x65ntries\x18\x01 \x03(\x0b\x32 .protowire.MempoolEntryByAddress\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\"\x1d\n\x1bGetCoinSupplyRequestMessage\"o\n\x1cGetCoinSupplyResponseMessage\x12\x10\n\x08maxSompi\x18\x01 \x01(\x04\x12\x18\n\x10\x63irculatingSompi\x18\x02 \x01(\x04\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCErrorB*Z(github.com/AnumaNetwork/anumad/protowireb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z(github.com/AnumaNetwork/anumad/protowire'
  _globals['_RPCERROR']._serialized_start=24
  _globals['_RPCERROR']._serialized_end=51
  _globals['_RPCBLOCK']._serialized_start=54
  _globals['_RPCBLOCK']._serialized_end=209
  _globals['_RPCBLOCKHEADER']._serialized_start=212
  _globals['_RPCBLOCKHEADER']._serialized_end=498
  _globals['_RPCBLOCKLEVELPARENTS']._serialized_start=500
  _globals['_RPCBLOCKLEVELPARENTS']._serialized_end=544
  _globals['_RPCBLOCKVERBOSEDATA']._serialized_start=547
  _globals['_RPCBLOCKVERBOSEDATA']._serialized_end=798
  _globals['_RPCTRANSACTION']._serialized_start=801
  _globals['_RPCTRANSACTION']._serialized_end=1061
  _globals['_RPCTRANSACTIONINPUT']._serialized_start=1064
  _globals['_RPCTRANSACTIONINPUT']._serialized_end=1262
  _globals['_RPCSCRIPTPUBLICKEY']._serialized_start=1264
  _globals['_RPCSCRIPTPUBLICKEY']._serialized_end=1326
  _globals['_RPCTRANSACTIONOUTPUT']._serialized_start=1329
  _globals['_RPCTRANSACTIONOUTPUT']._serialized_end=1488
  _globals['_RPCOUTPOINT']._serialized_start=1490
  _globals['_RPCOUTPOINT']._serialized_end=1541
  _globals['_RPCUTXOENTRY']._serialized_start=1544
  _globals['_RPCUTXOENTRY']._serialized_end=1673
  _globals['_RPCTRANSACTIONVERBOSEDATA']._serialized_start=1675
  _globals['_RPCTRANSACTIONVERBOSEDATA']._serialized_end=1791
  _globals['_RPCTRANSACTIONINPUTVERBOSEDATA']._serialized_start=1793
  _globals['_RPCTRANSACTIONINPUTVERBOSEDATA']._serialized_end=1825
  _globals['_RPCTRANSACTIONOUTPUTVERBOSEDATA']._serialized_start=1827
  _globals['_RPCTRANSACTIONOUTPUTVERBOSEDATA']._serialized_end=1921
  _globals['_GETCURRENTNETWORKREQUESTMESSAGE']._serialized_start=1923
  _globals['_GETCURRENTNETWORKREQUESTMESSAGE']._serialized_end=1956
  _globals['_GETCURRENTNETWORKRESPONSEMESSAGE']._serialized_start=1958
  _globals['_GETCURRENTNETWORKRESPONSEMESSAGE']._serialized_end=2053
  _globals['_SUBMITBLOCKREQUESTMESSAGE']._serialized_start=2055
  _globals['_SUBMITBLOCKREQUESTMESSAGE']._serialized_end=2145
  _globals['_SUBMITBLOCKRESPONSEMESSAGE']._serialized_start=2148
  _globals['_SUBMITBLOCKRESPONSEMESSAGE']._serialized_end=2347
  _globals['_SUBMITBLOCKRESPONSEMESSAGE_REJECTREASON']._serialized_start=2289
  _globals['_SUBMITBLOCKRESPONSEMESSAGE_REJECTREASON']._serialized_end=2347
  _globals['_GETBLOCKTEMPLATEREQUESTMESSAGE']._serialized_start=2349
  _globals['_GETBLOCKTEMPLATEREQUESTMESSAGE']._serialized_end=2420
  _globals['_GETBLOCKTEMPLATERESPONSEMESSAGE']._serialized_start=2422
  _globals['_GETBLOCKTEMPLATERESPONSEMESSAGE']._serialized_end=2546
  _globals['_NOTIFYBLOCKADDEDREQUESTMESSAGE']._serialized_start=2548
  _globals['_NOTIFYBLOCKADDEDREQUESTMESSAGE']._serialized_end=2580
  _globals['_NOTIFYBLOCKADDEDRESPONSEMESSAGE']._serialized_start=2582
  _globals['_NOTIFYBLOCKADDEDRESPONSEMESSAGE']._serialized_end=2652
  _globals['_BLOCKADDEDNOTIFICATIONMESSAGE']._serialized_start=2654
  _globals['_BLOCKADDEDNOTIFICATIONMESSAGE']._serialized_end=2721
  _globals['_GETPEERADDRESSESREQUESTMESSAGE']._serialized_start=2723
  _globals['_GETPEERADDRESSESREQUESTMESSAGE']._serialized_end=2755
  _globals['_GETPEERADDRESSESRESPONSEMESSAGE']._serialized_start=2758
  _globals['_GETPEERADDRESSESRESPONSEMESSAGE']._serialized_end=2968
  _globals['_GETPEERADDRESSESKNOWNADDRESSMESSAGE']._serialized_start=2970
  _globals['_GETPEERADDRESSESKNOWNADDRESSMESSAGE']._serialized_end=3021
  _globals['_GETSELECTEDTIPHASHREQUESTMESSAGE']._serialized_start=3023
  _globals['_GETSELECTEDTIPHASHREQUESTMESSAGE']._serialized_end=3057
  _globals['_GETSELECTEDTIPHASHRESPONSEMESSAGE']._serialized_start=3059
  _globals['_GETSELECTEDTIPHASHRESPONSEMESSAGE']._serialized_end=3156
  _globals['_GETMEMPOOLENTRYREQUESTMESSAGE']._serialized_start=3158
  _globals['_GETMEMPOOLENTRYREQUESTMESSAGE']._serialized_end=3261
  _globals['_GETMEMPOOLENTRYRESPONSEMESSAGE']._serialized_start=3263
  _globals['_GETMEMPOOLENTRYRESPONSEMESSAGE']._serialized_end=3372
  _globals['_GETMEMPOOLENTRIESREQUESTMESSAGE']._serialized_start=3374
  _globals['_GETMEMPOOLENTRIESREQUESTMESSAGE']._serialized_end=3465
  _globals['_GETMEMPOOLENTRIESRESPONSEMESSAGE']._serialized_start=3467
  _globals['_GETMEMPOOLENTRIESRESPONSEMESSAGE']._serialized_end=3580
  _globals['_MEMPOOLENTRY']._serialized_start=3582
  _globals['_MEMPOOLENTRY']._serialized_end=3675
  _globals['_GETCONNECTEDPEERINFOREQUESTMESSAGE']._serialized_start=3677
  _globals['_GETCONNECTEDPEERINFOREQUESTMESSAGE']._serialized_end=3713
  _globals['_GETCONNECTEDPEERINFORESPONSEMESSAGE']._serialized_start=3716
  _globals['_GETCONNECTEDPEERINFORESPONSEMESSAGE']._serialized_end=3845
  _globals['_GETCONNECTEDPEERINFOMESSAGE']._serialized_start=3848
  _globals['_GETCONNECTEDPEERINFOMESSAGE']._serialized_end=4068
  _globals['_ADDPEERREQUESTMESSAGE']._serialized_start=4070
  _globals['_ADDPEERREQUESTMESSAGE']._serialized_end=4131
  _globals['_ADDPEERRESPONSEMESSAGE']._serialized_start=4133
  _globals['_ADDPEERRESPONSEMESSAGE']._serialized_end=4194
  _globals['_SUBMITTRANSACTIONREQUESTMESSAGE']._serialized_start=4196
  _globals['_SUBMITTRANSACTIONREQUESTMESSAGE']._serialized_end=4298
  _globals['_SUBMITTRANSACTIONRESPONSEMESSAGE']._serialized_start=4300
  _globals['_SUBMITTRANSACTIONRESPONSEMESSAGE']._serialized_end=4394
  _globals['_NOTIFYVIRTUALSELECTEDPARENTCHAINCHANGEDREQUESTMESSAGE']._serialized_start=4396
  _globals['_NOTIFYVIRTUALSELECTEDPARENTCHAINCHANGEDREQUESTMESSAGE']._serialized_end=4490
  _globals['_NOTIFYVIRTUALSELECTEDPARENTCHAINCHANGEDRESPONSEMESSAGE']._serialized_start=4492
  _globals['_NOTIFYVIRTUALSELECTEDPARENTCHAINCHANGEDRESPONSEMESSAGE']._serialized_end=4585
  _globals['_VIRTUALSELECTEDPARENTCHAINCHANGEDNOTIFICATIONMESSAGE']._serialized_start=4588
  _globals['_VIRTUALSELECTEDPARENTCHAINCHANGEDNOTIFICATIONMESSAGE']._serialized_end=4773
  _globals['_GETBLOCKREQUESTMESSAGE']._serialized_start=4775
  _globals['_GETBLOCKREQUESTMESSAGE']._serialized_end=4842
  _globals['_GETBLOCKRESPONSEMESSAGE']._serialized_start=4844
  _globals['_GETBLOCKRESPONSEMESSAGE']._serialized_end=4942
  _globals['_GETSUBNETWORKREQUESTMESSAGE']._serialized_start=4944
  _globals['_GETSUBNETWORKREQUESTMESSAGE']._serialized_end=4995
  _globals['_GETSUBNETWORKRESPONSEMESSAGE']._serialized_start=4997
  _globals['_GETSUBNETWORKRESPONSEMESSAGE']._serialized_end=5082
  _globals['_GETVIRTUALSELECTEDPARENTCHAINFROMBLOCKREQUESTMESSAGE']._serialized_start=5084
  _globals['_GETVIRTUALSELECTEDPARENTCHAINFROMBLOCKREQUESTMESSAGE']._serialized_end=5196
  _globals['_ACCEPTEDTRANSACTIONIDS']._serialized_start=5198
  _globals['_ACCEPTEDTRANSACTIONIDS']._serialized_end=5282
  _globals['_GETVIRTUALSELECTEDPARENTCHAINFROMBLOCKRESPONSEMESSAGE']._serialized_start=5285
  _globals['_GETVIRTUALSELECTEDPARENTCHAINFROMBLOCKRESPONSEMESSAGE']._serialized_end=5508
  _globals['_GETBLOCKSREQUESTMESSAGE']._serialized_start=5510
  _globals['_GETBLOCKSREQUESTMESSAGE']._serialized_end=5604
  _globals['_GETBLOCKSRESPONSEMESSAGE']._serialized_start=5606
  _globals['_GETBLOCKSRESPONSEMESSAGE']._serialized_end=5727
  _globals['_GETBLOCKCOUNTREQUESTMESSAGE']._serialized_start=5729
  _globals['_GETBLOCKCOUNTREQUESTMESSAGE']._serialized_end=5758
  _globals['_GETBLOCKCOUNTRESPONSEMESSAGE']._serialized_start=5760
  _globals['_GETBLOCKCOUNTRESPONSEMESSAGE']._serialized_end=5868
  _globals['_GETBLOCKDAGINFOREQUESTMESSAGE']._serialized_start=5870
  _globals['_GETBLOCKDAGINFOREQUESTMESSAGE']._serialized_end=5901
  _globals['_GETBLOCKDAGINFORESPONSEMESSAGE']._serialized_start=5904
  _globals['_GETBLOCKDAGINFORESPONSEMESSAGE']._serialized_end=6178
  _globals['_RESOLVEFINALITYCONFLICTREQUESTMESSAGE']._serialized_start=6180
  _globals['_RESOLVEFINALITYCONFLICTREQUESTMESSAGE']._serialized_end=6246
  _globals['_RESOLVEFINALITYCONFLICTRESPONSEMESSAGE']._serialized_start=6248
  _globals['_RESOLVEFINALITYCONFLICTRESPONSEMESSAGE']._serialized_end=6325
  _globals['_NOTIFYFINALITYCONFLICTSREQUESTMESSAGE']._serialized_start=6327
  _globals['_NOTIFYFINALITYCONFLICTSREQUESTMESSAGE']._serialized_end=6366
  _globals['_NOTIFYFINALITYCONFLICTSRESPONSEMESSAGE']._serialized_start=6368
  _globals['_NOTIFYFINALITYCONFLICTSRESPONSEMESSAGE']._serialized_end=6445
  _globals['_FINALITYCONFLICTNOTIFICATIONMESSAGE']._serialized_start=6447
  _globals['_FINALITYCONFLICTNOTIFICATIONMESSAGE']._serialized_end=6512
  _globals['_FINALITYCONFLICTRESOLVEDNOTIFICATIONMESSAGE']._serialized_start=6514
  _globals['_FINALITYCONFLICTRESOLVEDNOTIFICATIONMESSAGE']._serialized_end=6586
  _globals['_SHUTDOWNREQUESTMESSAGE']._serialized_start=6588
  _globals['_SHUTDOWNREQUESTMESSAGE']._serialized_end=6612
  _globals['_SHUTDOWNRESPONSEMESSAGE']._serialized_start=6614
  _globals['_SHUTDOWNRESPONSEMESSAGE']._serialized_end=6676
  _globals['_GETHEADERSREQUESTMESSAGE']._serialized_start=6678
  _globals['_GETHEADERSREQUESTMESSAGE']._serialized_end=6759
  _globals['_GETHEADERSRESPONSEMESSAGE']._serialized_start=6761
  _globals['_GETHEADERSRESPONSEMESSAGE']._serialized_end=6842
  _globals['_NOTIFYUTXOSCHANGEDREQUESTMESSAGE']._serialized_start=6844
  _globals['_NOTIFYUTXOSCHANGEDREQUESTMESSAGE']._serialized_end=6897
  _globals['_NOTIFYUTXOSCHANGEDRESPONSEMESSAGE']._serialized_start=6899
  _globals['_NOTIFYUTXOSCHANGEDRESPONSEMESSAGE']._serialized_end=6971
  _globals['_UTXOSCHANGEDNOTIFICATIONMESSAGE']._serialized_start=6974
  _globals['_UTXOSCHANGEDNOTIFICATIONMESSAGE']._serialized_end=7107
  _globals['_UTXOSBYADDRESSESENTRY']._serialized_start=7109
  _globals['_UTXOSBYADDRESSESENTRY']._serialized_end=7235
  _globals['_STOPNOTIFYINGUTXOSCHANGEDREQUESTMESSAGE']._serialized_start=7237
  _globals['_STOPNOTIFYINGUTXOSCHANGEDREQUESTMESSAGE']._serialized_end=7297
  _globals['_STOPNOTIFYINGUTXOSCHANGEDRESPONSEMESSAGE']._serialized_start=7299
  _globals['_STOPNOTIFYINGUTXOSCHANGEDRESPONSEMESSAGE']._serialized_end=7378
  _globals['_GETUTXOSBYADDRESSESREQUESTMESSAGE']._serialized_start=7380
  _globals['_GETUTXOSBYADDRESSESREQUESTMESSAGE']._serialized_end=7434
  _globals['_GETUTXOSBYADDRESSESRESPONSEMESSAGE']._serialized_start=7436
  _globals['_GETUTXOSBYADDRESSESRESPONSEMESSAGE']._serialized_end=7560
  _globals['_GETBALANCEBYADDRESSREQUESTMESSAGE']._serialized_start=7562
  _globals['_GETBALANCEBYADDRESSREQUESTMESSAGE']._serialized_end=7614
  _globals['_GETBALANCEBYADDRESSRESPONSEMESSAGE']._serialized_start=7616
  _globals['_GETBALANCEBYADDRESSRESPONSEMESSAGE']._serialized_end=7706
  _globals['_GETBALANCESBYADDRESSESREQUESTMESSAGE']._serialized_start=7708
  _globals['_GETBALANCESBYADDRESSESREQUESTMESSAGE']._serialized_end=7765
  _globals['_BALANCESBYADDRESSENTRY']._serialized_start=7767
  _globals['_BALANCESBYADDRESSENTRY']._serialized_end=7862
  _globals['_GETBALANCESBYADDRESSESRESPONSEMESSAGE']._serialized_start=7865
  _globals['_GETBALANCESBYADDRESSESRESPONSEMESSAGE']._serialized_end=7993
  _globals['_GETVIRTUALSELECTEDPARENTBLUESCOREREQUESTMESSAGE']._serialized_start=7995
  _globals['_GETVIRTUALSELECTEDPARENTBLUESCOREREQUESTMESSAGE']._serialized_end=8044
  _globals['_GETVIRTUALSELECTEDPARENTBLUESCORERESPONSEMESSAGE']._serialized_start=8046
  _globals['_GETVIRTUALSELECTEDPARENTBLUESCORERESPONSEMESSAGE']._serialized_end=8152
  _globals['_NOTIFYVIRTUALSELECTEDPARENTBLUESCORECHANGEDREQUESTMESSAGE']._serialized_start=8154
  _globals['_NOTIFYVIRTUALSELECTEDPARENTBLUESCORECHANGEDREQUESTMESSAGE']._serialized_end=8213
  _globals['_NOTIFYVIRTUALSELECTEDPARENTBLUESCORECHANGEDRESPONSEMESSAGE']._serialized_start=8215
  _globals['_NOTIFYVIRTUALSELECTEDPARENTBLUESCORECHANGEDRESPONSEMESSAGE']._serialized_end=8312
  _globals['_VIRTUALSELECTEDPARENTBLUESCORECHANGEDNOTIFICATIONMESSAGE']._serialized_start=8314
  _globals['_VIRTUALSELECTEDPARENTBLUESCORECHANGEDNOTIFICATIONMESSAGE']._serialized_end=8412
  _globals['_NOTIFYVIRTUALDAASCORECHANGEDREQUESTMESSAGE']._serialized_start=8414
  _globals['_NOTIFYVIRTUALDAASCORECHANGEDREQUESTMESSAGE']._serialized_end=8458
  _globals['_NOTIFYVIRTUALDAASCORECHANGEDRESPONSEMESSAGE']._serialized_start=8460
  _globals['_NOTIFYVIRTUALDAASCORECHANGEDRESPONSEMESSAGE']._serialized_end=8542
  _globals['_VIRTUALDAASCORECHANGEDNOTIFICATIONMESSAGE']._serialized_start=8544
  _globals['_VIRTUALDAASCORECHANGEDNOTIFICATIONMESSAGE']._serialized_end=8612
  _globals['_NOTIFYPRUNINGPOINTUTXOSETOVERRIDEREQUESTMESSAGE']._serialized_start=8614
  _globals['_NOTIFYPRUNINGPOINTUTXOSETOVERRIDEREQUESTMESSAGE']._serialized_end=8663
  _globals['_NOTIFYPRUNINGPOINTUTXOSETOVERRIDERESPONSEMESSAGE']._serialized_start=8665
  _globals['_NOTIFYPRUNINGPOINTUTXOSETOVERRIDERESPONSEMESSAGE']._serialized_end=8752
  _globals['_PRUNINGPOINTUTXOSETOVERRIDENOTIFICATIONMESSAGE']._serialized_start=8754
  _globals['_PRUNINGPOINTUTXOSETOVERRIDENOTIFICATIONMESSAGE']._serialized_end=8802
  _globals['_STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDEREQUESTMESSAGE']._serialized_start=8804
  _globals['_STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDEREQUESTMESSAGE']._serialized_end=8860
  _globals['_STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDERESPONSEMESSAGE']._serialized_start=8862
  _globals['_STOPNOTIFYINGPRUNINGPOINTUTXOSETOVERRIDERESPONSEMESSAGE']._serialized_end=8956
  _globals['_BANREQUESTMESSAGE']._serialized_start=8958
  _globals['_BANREQUESTMESSAGE']._serialized_end=8989
  _globals['_BANRESPONSEMESSAGE']._serialized_start=8991
  _globals['_BANRESPONSEMESSAGE']._serialized_end=9048
  _globals['_UNBANREQUESTMESSAGE']._serialized_start=9050
  _globals['_UNBANREQUESTMESSAGE']._serialized_end=9083
  _globals['_UNBANRESPONSEMESSAGE']._serialized_start=9085
  _globals['_UNBANRESPONSEMESSAGE']._serialized_end=9144
  _globals['_GETINFOREQUESTMESSAGE']._serialized_start=9146
  _globals['_GETINFOREQUESTMESSAGE']._serialized_end=9169
  _globals['_GETINFORESPONSEMESSAGE']._serialized_start=9172
  _globals['_GETINFORESPONSEMESSAGE']._serialized_end=9333
  _globals['_ESTIMATENETWORKHASHESPERSECONDREQUESTMESSAGE']._serialized_start=9335
  _globals['_ESTIMATENETWORKHASHESPERSECONDREQUESTMESSAGE']._serialized_end=9420
  _globals['_ESTIMATENETWORKHASHESPERSECONDRESPONSEMESSAGE']._serialized_start=9422
  _globals['_ESTIMATENETWORKHASHESPERSECONDRESPONSEMESSAGE']._serialized_end=9538
  _globals['_NOTIFYNEWBLOCKTEMPLATEREQUESTMESSAGE']._serialized_start=9540
  _globals['_NOTIFYNEWBLOCKTEMPLATEREQUESTMESSAGE']._serialized_end=9578
  _globals['_NOTIFYNEWBLOCKTEMPLATERESPONSEMESSAGE']._serialized_start=9580
  _globals['_NOTIFYNEWBLOCKTEMPLATERESPONSEMESSAGE']._serialized_end=9656
  _globals['_NEWBLOCKTEMPLATENOTIFICATIONMESSAGE']._serialized_start=9658
  _globals['_NEWBLOCKTEMPLATENOTIFICATIONMESSAGE']._serialized_end=9695
  _globals['_MEMPOOLENTRYBYADDRESS']._serialized_start=9697
  _globals['_MEMPOOLENTRYBYADDRESS']._serialized_end=9823
  _globals['_GETMEMPOOLENTRIESBYADDRESSESREQUESTMESSAGE']._serialized_start=9825
  _globals['_GETMEMPOOLENTRIESBYADDRESSESREQUESTMESSAGE']._serialized_end=9946
  _globals['_GETMEMPOOLENTRIESBYADDRESSESRESPONSEMESSAGE']._serialized_start=9949
  _globals['_GETMEMPOOLENTRIESBYADDRESSESRESPONSEMESSAGE']._serialized_end=10082
  _globals['_GETCOINSUPPLYREQUESTMESSAGE']._serialized_start=10084
  _globals['_GETCOINSUPPLYREQUESTMESSAGE']._serialized_end=10113
  _globals['_GETCOINSUPPLYRESPONSEMESSAGE']._serialized_start=10115
  _globals['_GETCOINSUPPLYRESPONSEMESSAGE']._serialized_end=10226
# @@protoc_insertion_point(module_scope)
